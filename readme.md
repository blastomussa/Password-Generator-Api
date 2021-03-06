API Endpoint live at: https://blastomussa.dev/generate/api/v1 <br/>
HELP: https://blastomussa.dev/generate/api/help

<h1>Password Generator API</h1>
<p>Description: This API can be used to programatically generate passwords according to specified parameters</p>
<p>Example Usage: curl https://blastomussa.dev/generate/api/v1&quest;params=xxx&#38;param2=xxx</p>
<h3>Parameters List with defaults</h3>
<ol>
  <li>Maximum (int): max=18</li>
  <li>Minimum (int): min=8</li>
  <li>Number of Words (int): num_words=2</li>
  <li>Integers (bool): ints=true</li>
  <li>Number of Integers (int): num_ints=2</li>
  <li>Location of Integers (str)*: loc_ints=last</li>
  <li>Capital letters (bool): caps=true</li>
  <li>Number of Capitals (int): num_caps=1</li>
  <li>Location of Capitals (str)*: loc_caps=first</li>
  <li>Special Characters (bool): specs=true</li>
  <li>Number of Special Characters (int): num_specs=1</li>
  <li>Location of Special Characters (str)*: loc_specs=last</li>
  <li>Gibberish (bool): gib=false</li>
  <h4>* first, last, random</h4>
<ol/>
