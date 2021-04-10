---
title: "Lightouse weekly report {{ date | date('MMMM Do') | date('add', 3, 'days') }} - {{ date | date('add', 7, 'days') | date('Do') }}"
about: 'Are your scores flaky? You can run audits on Foo for stability and maintain a historical record! '
assignees: ivankatliarchuk
labels: ''
---

## Current Score
{{ env.SCORE }}


{{ env.URL }}

updated: {{ date | date('dddd, MMMM Do') }}
