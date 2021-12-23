# API Alerts

Api Alerts is a CLI tool to run checks against the Gemini API or other sources,
and report the data to stdout. Other checks and reporting mechanisms can be added.

## Requirements

Install the requirements.txt dependencies

```bash
pip install -r requirements.txt
```

## Usage

From root of directory:

```bash
./apiAlert -c <trading pair>
```

Examples:

```bash
./apiAlert -c btcusd
```

```bash
./apiAlert --help
```

## Approach
My approach to this solution happened in these steps:
- Understanding requirements
- Brief research of Gemini Public REST API
- Whiteboard design session to generate class structure
- Generation of boilerplate code
- Implementation of the various dependency classes and entry point
- Implementation of the check logic
- Fixing pylint errors

I went with an object oriented approach, as with these types of tools I can
see a high likelihood of someone needing to update this code or add a check
or source.

This class structure uses a basic Factory pattern to implement inversion of
control, allowing the checks to exist on their own with easy ability to add
new checks or edit existing ones, as well as switch out dependencies, like
other repos and result processors.

My intention was to have the time to implement some unit tests and create
a coded expectation of how these checks are to function. Unfortunately, I
ran out of time, but the unit tests are no less important.

## Issues faced
- Syntax
I didn't add parentheses to a couple of method calls which resulted in a JSON
serialization error, that took me a bit longer to figure out than necessary.

- Design
Originally I had set the timestamp to be created by the result processor at
the end of program execution, however I decided it would be more reliable to
pull the timestamp from the HTTP response object.
This is in case a bug is encountered that creates a delay between the request and the end of program execution.
This created some rework, as I didn't consider this during design.

- Parameters
I ran out of time to pass the deviation percentage parameter through.


Aside from those things and running out of time, the process went pretty smoothly


## To improve this

- Unit tests. This design takes unit testing into consideration, so that it should be easy to test various cases.
- Depending on the development environment and context, I would create more a more formal interface for classes, so that coding to interface is preferred and coding to implementation is less likely. Otherwise, it may be acceptable to drop the parent classes for repos and result processors, to simplify.
- Pylint
I created docstrings as they are required by pylint, but my initial goal was
to have the code be fairly self-explanatory, in which case the docstrings may
be making this less readable than more. I would spend more time on making those
more clear or readable.
- Parameters
Currently any argument is accepted as a trading pair. This will result in an error and an unneeded call to the API.
I would have a set of allowed trading pairs. Or if this is enough of a problem in its environment, have a separate code path to refresh a list of currently available trading pairs.
Separately, this needs to have a deviation percentage threshold parameter added.
- Logging
Didn't have enough time to get a log level switch and logging statements into the application itself. Those would be useful.
- Create a python wheel and allow it to be installed through pip
- Add a virtualenv config for development purposes.


## Other checks to add
- Check against recent trade count - crypto trades 24/7, there should always be trades. Reviewing historic data to understand what is unusual and warrants human attention would help to determine the threshold, and this tool would only need to report the trade count from the "trades" endpoint
- Add a source to another exchange and compare price data. Different exchanges have different prices, but at a certain extreme threshold, this may be worth alerting on.
- Volume alerts may be useful to help understand load.

## Time taken
About 4 hours including design and implementation. I probably went a little over (~15 min) fixing pylint errors.
