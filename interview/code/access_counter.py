In a server, I would like to get running counters of how often an event occurred in the last second, the last minute, and the last hour.
This could be used for a debug page on how much traffic there is right now:

Page          | s   | m   | h
------------- | --- | --- | ----
/index.html   | 10  | 400 | 5000
/profile.html | 1   | 7   | 99

This means that /index.html was viewed 10 times in the last second, 400 times in the last minute (i.e. the previous 60s) and 5000 times in the last hour (i.e. the previous 60min).
The numbers should reflect what is happening on the server right now and be updated continuously.

Additional Information
- The advancing function is called by an external clock system, once per second
- External use is thread-safe, no need to discuss it

class SMHCOUNTER:
  """should give a value at any given point in time
  """
  SECONDS_IN_AN_HOUR = 60 * 60
  def __init__(self):
    """
    Args
      _values contains elements for last hour
      _offset points to current second in the array
    """
    self._values = []
    for x in range(SMHCOUNTER.SECONDS_IN_AN_HOUR):
      self._values.append(0)
    self._offset = 0
    self._minute = 0


  def advance(self):
    """The advancing function is called by an external system
    """
    self._offset += 1
    if self._offset > SMHCOUNTER.SECONDS_IN_AN_HOUR:
      self._offset = 0
    self._values[offset] = 0

  def inc(self):
    """on every event that is happening
    """
    self._values[self._offset] += 1

  def get_counter(self, time_duration:str): -> int
    """provide a number of requests at last second, munite or an hour

    Args:
      v : it could be s, m, h
    Raises:
      Value erorr if time duration not supported
    Return: The current nubmer of requests of type int # todo: edge case integer overflow
    """
    if time_duration not in ['s', 'm', 'h']:
      raise ValueError("time duration not supported")

    result = 0
     # todo: test if case for this scenario
    if time_duration == 's':
      # todo: test case for this scenario
      result = self._values[self._offset]
    elif time_duration == 'm':
      # will get last 60 seconds, will exclude minute + 1 second and iterate over every second
      for x in range(self._offset - 59, self._offset + 1):
        if x >= 0:
          # when there is no array overflow will add events to a result for a given second
          result += self._values[x]
        else:
          # pull the code
          result += self._values[x]
    else:
      for x in range(self._offset - 3600, self._offset):
        if x >= 0:
          result += self._values[self._offset]
        else:
          result += self._values[3600 - x]

    return result

  Tests


  _values[-1] --> last element of the array

