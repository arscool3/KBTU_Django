# PdfService

PdfService is a service to generate pdfs by getting and aggregating data from different resources.

## Installation

Clone the project from this repository.

```bash
git clone --branch pdf-generator-service https://gitlab.com/di-halyk-academy-maglnuse/maglnuse-egov.git
```

## Setup and Using

Create virtualenv

```bash
virtualenv venv
```

Activate virtualenv

```bash
source venv/bin/activate
```

After installing all dependencies of packages
create a ```.env``` file in your project root folder

in this file you have to store all your secrets


Then run

```bash
python main.py
```

and go to the 
```url
0.0.0.0:8000/docs
```

there you can see all of your available methods and endpoints
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
### Let's create something interesting together
## License

[MIT](https://choosealicense.com/licenses/mit/)