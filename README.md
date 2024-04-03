# Pre 2000 games from Swiss Games Garden
 
A project that extracts all pre 2000 games on the [Swiss Games Garden](https://swissgames.garden/) website into an excel sheet using their API.

## Remarks

Since the API doesn't allow full access to Swiss Games Garden's data, some of the fields in the excel sheet are left blank.

The variable containing all the links to the API responses is not very elegant, but since the data doesn't have a `next` key I had to manually check all the pages containing data te retrieve them.

## Installation

We advise you to work in a virtualenv. To install the `requirements.txt` file, run the following command in a terminal:

- Unix/macOS: `python3 -m pip install -r requirements.txt`
- Windows: `py -m pip install -r requirements.txt`

## License

Distributed under the MIT License. See LICENSE.txt for more information.

## Credits

Made by Johan Cuda, student assistant in the [CH Ludens](https://chludens.ch/) Sinergia project.