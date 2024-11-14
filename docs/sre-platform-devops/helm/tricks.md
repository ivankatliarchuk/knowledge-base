---
title: helm
summary: Making the most out of Helm templates
authors: ["ivan k"]
tags: ["helm", "kubernetes", "platform"]
date: 2024-11-14
source:
- https://blog.palark.com/advanced-helm-templating/
published: true
---

The standard Helm library and traditional approaches to creating Helm charts are generally okay to automate non-complex tasks. But the growing complexity and number of Helm charts rapidly make the minimalistic Helm templates and controversial standard Helm library insufficient. In this article, we will show you how to make your Helm templates much more flexible and dynamic by implementing your own Helm “functions” and exploiting the capabilities of the `tpl` function.

**_NB_**_: All the examples below were tested to work in the_ [_werf_](https://werf.io/) _CI/CD tool that uses Helm “under the hood” to deploy to Kubernetes. Since werf templates are almost identical to those of Helm, all the snippets below are expected to be compatible with both versions of Helm (v2 & v3)._

Now, let’s look at how Helm templates can help you to do some amazing things!

## 1\. Include/define templates as full-fledged functions

The `define` function allows you to reuse some common parts of templates. In most cases, the usage of `define` (and accompanying `include`) is limited to isolating elementary template snippets such as annotations, labels, resource names.

However, you can turn `define` into a full-fledged function and abstract the logic into it.

### 1.1. Passing arguments

While `include` accepts only one argument, you can also pass to it a list of multiple arguments:

```bash
{{- include "testFunc" (list $val1 $val2) }}
```

… and then access those arguments inside the template in the following manner:

```bash
{{- define "testFunc" }} {{- $arg1 := index . 0 }} {{- $arg2 := index . 1 }}
```

Here is a complete example:

```bash
{{- define "testFunc" }} {{- $arg1 := index . 0 }} {{- $arg2 := index . 1 }} # Combine arguments into a string and return the result: {{ print $arg1 $arg2 }} {{- end }} --- {{- $val1 := "foo" }} {{- $val2 := "bar" }} {{- include "testFunc" (list $val1 $val2) }} # ==> string "foobar"
```

### 1.2. Passing the current and root context

Root context (`$`) is a dictionary that contains all [built-in objects](https://helm.sh/docs/chart_template_guide/builtin_objects/), including the `Values` object. The current context (`.`) points to the root context by default, but the user can change which variable the current context points to.

Inside the template, the argument passed to `include` (or, in our case, a list of arguments) becomes the current (and root) context. However, in this case, we do not have access to other contexts (not even `$.Values`) inside the template except for the list of arguments. However, there is a way around this: just pass the contexts via the argument list.

```bash
{{- include "testFunc" (list $ . $arg) }}
```

Now you can restore the root context (so that it can be accessed via `$`):

```bash
{{- define "testFunc" }} {{- $ := index . 0 }}
```

… as well as the current context (and access it via `.`):

```undefined
{{- with index . 1 }}
```

In the end, we will get the following:

```yaml
.helm/values.yaml: ------------------------------------------------------------- key: "value" ------------------------------------------------------------- .helm/templates/testFunc.yaml: ------------------------------------------------------------- {{- define "testFunc" }} {{- $ := index . 0 }} {{- $stringArg := index . 2 }} {{- with index . 1 }} # Now we have access to the "real" root and current contexts # just as if we were outside of include/define: {{ cat $stringArg $.Values.key .Values.key }} {{- end }} {{- end }} --- {{- $arg := "explicitlyPassed" }} {{- include "testFunc" (list $ . $arg) }} # ==> string "explicitlyPassed value value"
```

### 1.3. Passing optional arguments

There are several ways to pass optional arguments to a template. The most flexible and convenient one is to pass a dictionary with optional arguments in the list of arguments:

```bash
{{- include "testFunc" (list $requiredArg (dict "optionalArg2" "optionalValue2")) }}
```

Let’s add some magic to our template so that it can handle the absence of optional arguments:

```bash
{{- define "testFunc" }} ... {{- $optionalArgs := dict }} {{- if ge (len .) 2 }}{{ $optionalArgs = index . 1 }}{{ end }}
```

Now you can access optional arguments using the `{{ $optionalArgs.optionalArg2 }}` construction. Here is a complete example:

```bash
{{- define "testFunc" }} {{- $requiredArg := index . 0 }} {{- $optionalArgs := dict }} {{- if ge (len .) 2 }}{{ $optionalArgs = index . 1 }}{{ end }} # Check for the optional arguments # and use them if they are available: {{- if hasKey $optionalArgs "optionalArg1" }} {{- cat "Along with" $requiredArg "we have at least" $optionalArgs.optionalArg1 }} {{- else if hasKey $optionalArgs "optionalArg2" }} {{- cat "Along with" $requiredArg "we have" $optionalArgs.optionalArg2 }} {{- else }} {{- cat "We only have" $requiredArg }} {{- end }} {{- end }} --- {{- $requiredArg := "requiredValue" }} # Let’s include the template that does not have optional arguments: {{- include "testFunc" (list $requiredArg) }} # ==> string "We only have requiredValue" # Now, let’s include the template that does have one of two optional arguments: {{- include "testFunc" (list $requiredArg (dict "optionalArg2" "optionalValue2")) }} # ==> string "Along with requiredValue we have optionalValue2"
```

### 1.4. Nested includes and recursion

You can `include` other templates from within the template. This applies to the original template as well. In other words, you can include templates recursively (similarly to common programming languages):

```yaml
{{- define "testFunc" }} {{- $num := . }} {{- if lt $num 10 }} # Include the different template: {{- include "print" $num }} # Include the current (active) template recursively {{- include "testFunc" (add 1 $num) }} {{- end }} {{- end }} {{- define "print" }} {{- print . }} {{- end }} --- {{- include "testFunc" 0 }} # ==> string "0123456789"
```

### 1.5. Returning common data types from templates

The way `include` works is very straightforward: `{{ include }}` is substituted with the text rendered in the template. By default, you can’t return anything other than a string from the template. Thus, you cannot return a list or a dictionary inside the dictionary (to cycle through its values later). However, there is a workaround that involves serialization.

To use it, you have to serialize data into JSON (or YAML) inside the template:

```bash
{{- define "returnJson" }} {{- $result := dict "key1" (dict "nestedKey1" "nestedVal1") }} {{- $result | toJson }} {{- end }}
```

The serialized data is returned as a string when this template is called. Let’s check it:

```bash
{{ include "returnJson" . | typeOf }} # ==> string "string"
```

Now we can de-serialize the string received from the template and see what data type it has:

```bash
{{- include "returnJson" . | fromJson | typeOf }} # ==> string "map[string]interface {}"
```

As you can see, it is not just a string, but a dictionary with another dictionary nested in it. Thus, you can use the usual dictionary functions on it:

```bash
{{- include "returnJson" . | fromJson | values }} # ==> string "[map[nestedKey1:nestedVal1]]"
```

You can use the above approach to serialize any data types: lists, dictionaries, boolean values, etc. (including nested values).

## 1.6. Using include in if-else conditional constructs and the ternary function

When used in conditions of `if` blocks, `include` returns strings only and does not convert them to other data types. In other words, if the boolean `true` is returned from the template, it becomes the string `"true"`. Any non-empty string is equivalent to boolean `true` in the `if` block condition. Note that if the boolean `false` is returned from the template, it becomes a non-empty `"false"` string, which itself means a boolean `true`.

If you want to get a real boolean `false` in the `if` condition, you can return an _empty_ string from the template:

```bash
{{- define "returnPseudoBoolean" }} {{- if eq . "pleaseReturnTrue" }} true {{- else if eq . "pleaseReturnFalse" }} {{- end }} {{- end }}
```

This way, you can implement includes that will be evaluated in the conditions of `if` blocks.

```bash
{{- if include "returnPseudoBoolean" "pleaseReturnTrue" }} {{- print "The first if returns True" }} {{- end }} # ==> string "The first if returns True" {{- if include "returnPseudoBoolean" "pleaseReturnFalse" }} {{- else }} {{- print "The second if returns False" }} {{- end }} # ==> string "The second if returns False"
```

The `ternary` function works the other way. It expects to get a real boolean value at the input and not a string. You can return boolean values from the template by feeding the template output to the `empty` function. This is similar to how `if` conditions work:

```bash
{{- ternary "Here is True" "Here is False" (include "returnBoolean" "pleaseReturnTrue" | not | empty) }} # ==> string "Here is True"
```

## 2\. Using the tpl function effectively

The `tpl` function is a powerful tool for templating in cases where it was not possible before. It has proved to be effective for using values from `values.yaml` in templates. However, this function has several limitations that prevent it from reaching its full potential. Let’s take a look at those limitations and discuss ways to overcome them.

### 2.1. Making a wrapper for Values

Let’s put our wrapper logic for the `tpl` function into the template to re-use it. Let’s call it `value` and use it as a wrapper for all our `Values`. Now we can use `{{ include "value" (list $ . $.Values.key }}` in place of `{{ $.Values.key }}`.

The template itself looks like this:

```yaml
.helm/values.yaml: ------------------------------------------------------------- key1: "Value of key2: {{ $.Values.key2 }}" key2: "value2" ------------------------------------------------------------- .helm/templates/test.yaml: ------------------------------------------------------------- {{- define "value" }} # Let’s pass the contexts - we will need them later: {{- $ := index . 0 }} {{- $val := index . 2 }} {{- with index . 1 }} {{- tpl $val $ }} {{- end }} {{- end }} --- {{- include "value" (list $ . $.Values.key1) }} # ==> String "Value of key2: value2"
```

For now, we just pass the third argument of the template to the `tpl` function. This argument is just a value. This way, we can get the desired result.

_**NB**: We will not be implementing the processing of other data types (non-string) in the `value` template. You can implement wrappers for other data types yourselves using constructions similar to `{{- if kindIs "map" $val }}`._

### 2.2. Passing the current context

The `tpl` function _only_ accepts a dictionary containing a [Template object](https://helm.sh/docs/chart_template_guide/builtin_objects/) as an argument. This dictionary is the root context (`$`). It is usually passed as an argument to the `tpl` function. In this case, we cannot use the trick with passing a list of several nested arguments because this list will not contain the required `Template` object. Yet, there are several ways to pass the current context along with the root one. Let’s take a look at the simplest one.

The first step is to create a new key in the root context with the _current_ context as a value, and then pass the root context to `tpl`. In this case, the `{{- tpl $val $ }}` expression would turn into:

```bash
{{- tpl $val (merge (dict "RelativeScope" .) $) }}
```

Now you can access the local context using `{{ $.RelativeScope }}` in our `$val` template-string that is passed to the `tpl` function for rendering.

The second step is to wrap the `$val` template-string using a `with` block. It would restore the current context and make it accessible via the dot (`.`):

```bash
{{- tpl (cat "{{- with $.RelativeScope -}}" $val "{{- end }}") (merge (dict "RelativeScope" .) $) }}
```

And now you can use the root as well as the relative context in `values.yaml`:

```yaml
.helm/values.yaml: ------------------------------------------------------------- key1: "Value of key2: {{ .key2 }}" key2: "value2" ------------------------------------------------------------- .helm/templates/test.yaml: ------------------------------------------------------------- {{- define "value" }} {{- $ := index . 0 }} {{- $val := index . 2 }} {{- with index . 1 }} {{- tpl (cat "{{- with $.RelativeScope -}}" $val "{{- end }}") (merge (dict "RelativeScope" .) $) }} {{- end }} {{- end }} --- # Switching the current context: {{- with $.Values }} # Let’s try to use a relative path to key1: {{- include "value" (list $ . .key1) }} {{- end }} # ==> String "Value of key2: value2"
```

The access to the current context comes in handy, e.g., for cyclical generating of YAML snippets. In this case, you often need access to the context under the current iteration.

In a similar way, you can pass any additional arguments to the `tpl` function. You just have to attach those arguments to the root context and pass the roo context to the `tpl` function.

### 2.3. tpl performance issues

There are known performance issues related to the `tpl` function (more details are in [this issue](https://github.com/helm/helm/issues/8002)). That is why calling `tpl` for each `Value` (even if it is unnecessary) can significantly slow down the rendering of large charts. You can check for `{{` in the template-string to avoid unnecessary calls of the `tpl` function. If there are no curly brackets in the template-string, the value is returned from the `value` template as is, and no passing to the `tpl` function is performed:

```yaml
{{- define "value" }} {{- $ := index . 0 }} {{- $val := index . 2 }} {{- with index . 1 }} {{- if contains "{{" $val }} {{- tpl (cat "{{- with $.RelativeScope -}}" $val "{{- end }}") (merge (dict "RelativeScope" .) $) }} {{- else }} {{- $val }} {{- end }} {{- end }} {{- end }} --- {{- with $.Values }} {{- include "value" (list $ . .key1) }} {{- end }}
```

On the other hand, if there are curly brackets in the template-string, then it is passed to the `tpl` function for processing. Such an elementary trick helps to speed up template rendering significantly.

## 3\. Debugging

Debugging becomes much more complicated with growing amounts of logic in charts. In addition to the regular `helm render` and `helm lint`, there is also the `fail` function. Often, it is the best alternative to the ordinary `{{ $valueToDump }}`. The `fail` function does not require charts to be rendered without errors and can be used anywhere. It immediately produces the result without having to pass it to the manifest. You just need to be able to call this function during the rendering process.

Here is how you can dump the current context:

```yaml
{{- fail (toYaml $.Values) }} # ==> "key1: val1 # key2: val2 # ...."
```

And here is how to use it for debugging cycles/recursions (the order is not preserved; however, you can sort the output by timestamp):

```bash
{{- range (list "val1" "val2") }} {{- $_ := set $.Values.global (toString now) (toYaml .) }} {{- end }} {{ fail (toYaml $.Values.global) }} # ==> "2020-12-12 19:52:10.750813319 +0300 MSK m=+0.202723745: | # val1 # 2020-12-12 19:52:10.750883773 +0300 MSK m=+0.202794200: | # val2"
```

Similarly, you can save any intermediate results and later print them using the `fail` function:

```bash
{{- $_ := set $.Values.global "value1" $val1 }} {{- $_ := set $.Values.global "value2" $val2 }} {{ fail (toYaml $.Values.global) }} # ==> "value1: val1 # value2: val2"
```

## Key takeaways

I don’t really like the nowadays prevalent approach to generating the YAML code using the general-purpose (and quite mediocre, TBH) template engines that do not “_understand_” YAML. YAML is not designed to be generated as a text from a template, and the fact that this practice has become ubiquitous (while inappropriate) just upsets me. Still, you often have to use the tools and methods _available_ to the maximum. This article shows how to get the most flexibility and dynamics out of Helm templates.

If you feel that the methods discussed above are not enough to make charts maintainable and expandable, then you might want to try to generate YAML programmatically by substituting the generated manifests similar to the way the deployment software does that. [Cdk8s](https://blog.palark.com/cdk8s-framework-for-kubernetes-manifests/) is a perfect example of software-based generating of “pure Kubernetes” YAML. While it is an early-stage project, cdk8s demonstrates the potential of this idea. But while we are waiting with trepidation for the bright and template-less YAML future, we should not be embarrassed to exploit template engines that, in turn, have been exploiting us for ages.
