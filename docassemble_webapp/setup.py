import os
import sys
from setuptools import setup, find_namespace_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup_requires = [
    'enum34==1.1.10'
    ]
install_requires = [
    'docassemble==1.6.0',
    'docassemble.base==1.6.0',
    'docassemble.demo==1.6.0',
    "3to2==1.1.1",
    "acme==3.0.1",
    "aiohappyeyeballs==2.4.3",
    "aiohttp==3.11.8",
    "aiohttp-retry==2.8.3",
    "aiosignal==1.3.1",
    "airtable-python-wrapper==0.15.3",
    "alembic==1.14.0",
    "amqp==5.3.1",
    "anyio==4.6.2.post1",
    "argon2-cffi==23.1.0",
    "argon2-cffi-bindings==21.2.0",
    "asn1crypto==1.5.1",
    "astunparse==1.6.3",
    "async-generator==1.10",
    "async-timeout==5.0.1",
    "atomicwrites==1.4.1",
    "attrs==24.2.0",
    "azure-common==1.1.28",
    "azure-core==1.32.0",
    "azure-identity==1.19.0",
    "azure-keyvault-secrets==4.9.0",
    "azure-nspkg==3.0.2",
    "azure-storage-blob==12.24.0",
    "babel==2.16.0",
    "backports.tarfile==1.2.0",
    "bcrypt==4.2.1",
    "beautifulsoup4==4.12.3",
    "behave==1.2.6",
    "bidict==0.23.1",
    "billiard==4.2.1",
    "black==24.10.0",
    "bleach==6.2.0",
    "blinker==1.9.0",
    "boto==2.49.0",
    "boto3==1.35.71",
    "botocore==1.35.71",
    "build==1.2.2.post1",
    "cachetools==5.5.0",
    "cairocffi==1.7.1",
    "CairoSVG==2.7.1",
    "celery==5.4.0",
    "certbot==3.0.1",
    "certbot-apache==3.0.1",
    "certbot-nginx==3.0.1",
    "certifi==2024.8.30",
    "cffi==1.17.1",
    "chardet==5.2.0",
    "charset-normalizer==3.4.0",
    "click==8.1.7",
    "click-didyoumean==0.3.1",
    "click-plugins==1.1.1",
    "click-repl==0.3.0",
    "clicksend-client==5.0.78",
    "colorama==0.4.6",
    "commonmark==0.9.1",
    "ConfigArgParse==1.7",
    "configobj==5.0.9",
    "configparser==7.1.0",
    "contourpy==1.3.1",
    "convertapi==2.0.0",
    "crayons==0.4.0",
    "cryptography==44.0.0",
    "cssselect2==0.7.0",
    "cycler==0.12.1",
    "defusedxml==0.7.1",
    "Deprecated==1.2.15",
    "deprecation==2.1.0",
    "distro==1.9.0",
    "dnspython==2.7.0",
    "docassemble-backports==1.0",
    "Docassemble-Flask-User==0.6.30",
    "Docassemble-Pattern==3.6.7",
    "docassemble-textstat==0.7.2",
    "docassemblekvsession==0.9",
    "docopt==0.6.2",
    "docutils==0.21.2",
    "docxcompose==1.4.0",
    "docxtpl==0.19.0",
    "email_validator==2.2.0",
    "et_xmlfile==2.0.0",
    "eventlet==0.38.0",
    "exceptiongroup==1.2.2",
    "Flask==3.1.0",
    "flask-babel==4.0.0",
    "Flask-Cors==5.0.0",
    "Flask-Login==0.6.3",
    "Flask-Mail==0.10.0",
    "Flask-SocketIO==5.4.1",
    "Flask-SQLAlchemy==3.1.1",
    "Flask-WTF==1.2.2",
    "fonttools==4.55.0",
    "frozenlist==1.5.0",
    "future==1.0.0",
    "gcs-oauth2-boto-plugin==3.2",
    "geographiclib==2.0",
    "geopy==2.4.1",
    "google-api-core==2.23.0",
    "google-api-python-client==2.154.0",
    "google-auth==2.17.0",
    "google-auth-httplib2==0.2.0",
    "google-auth-oauthlib==1.2.1",
    "google-cloud-core==2.4.1",
    "google-cloud-storage==2.11.0",
    "google-cloud-translate==3.18.0",
    "google-cloud-vision==3.8.1",
    "google-crc32c==1.6.0",
    "google-i18n-address==3.1.1",
    "google-reauth==0.1.1",
    "google-resumable-media==2.7.2",
    "googleapis-common-protos==1.66.0",
    "greenlet==3.1.1",
    "grpc-google-iam-v1==0.13.1",
    "grpcio==1.68.0",
    "grpcio-status==1.68.0",
    "gspread==6.1.4",
    "guess-language-spirit==0.5.3",
    "h11==0.14.0",
    "httpcore==1.0.7",
    "httplib2==0.22.0",
    "humanize==4.11.0",
    "Hyphenate==1.1.0",
    "idna==3.10",
    "img2pdf==0.5.1",
    "importlib_metadata==8.5.0",
    "importlib_resources==6.4.5",
    "iniconfig==2.0.0",
    "iso8601==2.1.0",
    "isodate==0.7.2",
    "itsdangerous==2.2.0",
    "jaraco.classes==3.4.0",
    "jaraco.context==6.0.1",
    "jaraco.functools==4.1.0",
    "jdcal==1.4.1",
    "jeepney==0.8.0",
    "jellyfish==1.1.0",
    "Jinja2==3.1.4",
    "jmespath==1.0.1",
    "joblib==1.4.2",
    "josepy==1.14.0",
    "keyring==25.5.0",
    "kombu==5.4.2",
    "libcst==1.5.1",
    "links-from-link-header==0.1.0",
    "lxml==5.3.0",
    "Mako==1.3.6",
    "Markdown==3.7",
    "markdown-it-py==3.0.0",
    "MarkupSafe==3.0.2",
    "mdurl==0.1.2",
    "minio==7.2.12",
    "monotonic==1.6",
    "more-itertools==10.5.0",
    "msal==1.31.1",
    "msal-extensions==1.2.0",
    "msrest==0.7.1",
    "multidict==6.1.0",
    "mypy-extensions==1.0.0",
    "namedentities==1.9.4",
    "netifaces==0.11.0",
    "nh3==0.2.19",
    "nltk==3.9.1",
    "num2words==0.5.13",
    "numpy==2.1.3",
    "oauth2client==4.1.3",
    "oauthlib==3.2.2",
    "openpyxl==3.1.5",
    "ordered-set==4.1.0",
    "outcome==1.3.0.post0",
    "packaging==24.2",
    "pandas==2.2.3",
    "parse==1.20.2",
    "parse_type==0.6.4",
    "parsedatetime==2.6",
    "passlib==1.7.4",
    "pathspec==0.12.1",
    "pdfminer.six==20240706",
    "phonenumbers==8.13.50",
    "pikepdf==9.4.2",
    "pillow==11.0.0",
    "pkginfo==1.11.2",
    "platformdirs==4.3.6",
    "pluggy==1.5.0",
    "ply==3.11",
    "portalocker==2.10.1",
    "prompt_toolkit==3.0.48",
    "propcache==0.2.0",
    "proto-plus==1.25.0",
    "protobuf==5.29.0",
    "psutil==6.1.0",
    "psycopg2-binary==2.9.10",
    "pyasn1==0.6.1",
    "pyasn1_modules==0.4.1",
    "pycountry==24.6.1",
    "pycparser==2.22",
    "pycryptodome==3.21.0",
    "pycryptodomex==3.21.0",
    "Pygments==2.18.0",
    "PyJWT==2.10.1",
    "PyLaTeX==1.4.2",
    "PyNaCl==1.5.0",
    "pyOpenSSL==24.3.0",
    "pyotp==2.9.0",
    "pyparsing==3.2.0",
    "pypng==0.20220715.0",
    "pyproject_hooks==1.2.0",
    "pyRFC3339==2.0.1",
    "PySocks==1.7.1",
    "pytest==8.3.3",
    "python-augeas==1.1.0",
    "python-dateutil==2.9.0.post0",
    "python-docx==1.1.2",
    "python-dotenv==1.0.1",
    "python-editor==1.0.4",
    "python-engineio==4.10.1",
    "python-http-client==3.3.7",
    "python-ldap==3.4.4",
    "python-socketio==5.11.4",
    "pytz==2024.2",
    "pytz-deprecation-shim==0.1.0.post0",
    "pyu2f==0.1.5",
    "PyYAML==6.0.2",
    "pyzbar==0.1.9",
    "qrcode==8.0",
    "rauth==0.7.3",
    "readme_renderer==44.0",
    "redis==5.2.0",
    "regex==2024.11.6",
    "reportlab==4.2.5",
    "repoze.lru==0.7",
    "requests==2.32.3",
    "requests-oauthlib==2.0.0",
    "requests-toolbelt==1.0.0",
    "retry-decorator==1.1.1",
    "rfc3339==6.2",
    "rfc3986==2.0.0",
    "rich==13.9.4",
    "rsa==4.7.2",
    "ruamel.yaml==0.18.6",
    "ruamel.yaml.bytes==0.1.0",
    "ruamel.yaml.clib==0.2.12",
    "ruamel.yaml.string==0.1.1",
    "s3transfer==0.10.4",
    "s4cmd==2.1.0",
    "scikit-learn==1.5.2",
    "scipy==1.14.1",
    "SecretStorage==3.3.3",
    "selenium==4.27.1",
    "sendgrid==6.11.0",
    "simple-websocket==1.1.0",
    "simplekv==0.14.1",
    "six==1.16.0",
    "sniffio==1.3.1",
    "SocksiPy-branch==1.1",
    "sortedcontainers==2.4.0",
    "soupsieve==2.6",
    "SQLAlchemy==2.0.36",
    "starkbank-ecdsa==2.2.0",
    "tailer==0.4.1",
    "telnyx==2.1.3",
    "threadpoolctl==3.5.0",
    "tinycss2==1.4.0",
    "titlecase==2.4.1",
    "toml==0.10.2",
    "tomli==2.2.1",
    "tqdm==4.67.1",
    "trio==0.27.0",
    "trio-websocket==0.11.1",
    "twilio==9.3.7",
    "twine==6.0.0",
    "types-python-dateutil==2.9.0.20241003",
    "typing-inspect==0.9.0",
    "typing_extensions==4.12.2",
    "tzdata==2024.2",
    "tzlocal==5.2",
    "ua-parser==1.0.0",
    "ua-parser-builtins==0.18.0",
    "uritemplate==4.1.1",
    "urllib3==2.2.3",
    "us==3.2.0",
    "user-agents==2.2.0",
    "uWSGI==2.0.28",
    "vine==5.1.0",
    "wcwidth==0.2.13",
    "webdriver-manager==4.0.2",
    "webencodings==0.5.1",
    "websocket-client==1.8.0",
    "Werkzeug==3.1.3",
    "wrapt==1.17.0",
    "wsproto==1.2.0",
    "WTForms==3.2.1",
    "xfdfgen==0.4",
    "xlrd==2.0.1",
    "XlsxWriter==3.2.0",
    "xlwt==1.3.0",
    "yarl==1.18.0",
    "zipp==3.21.0"
]

setup(name='docassemble.webapp',
      version='1.6.0',
      python_requires='>=3.9',
      description=('The web application components of the docassemble system.'),
      long_description=read("README.md"),
      long_description_content_type='text/markdown',
      author='Jonathan Pyle',
      author_email='jhpyle@gmail.com',
      license='MIT',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=install_requires,
      zip_safe=False,
      package_data={'docassemble.webapp': ['alembic.ini', os.path.join('alembic', '*'), os.path.join('alembic', 'versions', '*'), os.path.join('data', '*.*'), os.path.join('data', 'static', '*.*'), os.path.join('data', 'static', 'favicon', '*.*'), os.path.join('data', 'questions', '*.*'), os.path.join('templates', 'base_templates', '*.html'), os.path.join('templates', 'flask_user', '*.html'), os.path.join('templates', 'flask_user', 'emails', '*.*'), os.path.join('templates', 'pages', '*.html'), os.path.join('templates', 'pages', '*.xml'), os.path.join('templates', 'pages', '*.js'), os.path.join('templates', 'users', '*.html'), os.path.join('static', 'app', '*.*'), os.path.join('static', 'sounds', '*.*'), os.path.join('static', 'examples', '*.*'), os.path.join('static', 'examplesdark', '*.*'), os.path.join('static', 'fontawesome', 'js', '*.*'), os.path.join('static', 'office', '*.*'), os.path.join('static', 'bootstrap-fileinput', 'img', '*'), os.path.join('static', 'img', '*'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'locales', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'plugins', '*'), os.path.join('static', 'bootstrap-slider', 'dist', '*.js'), os.path.join('static', 'bootstrap-slider', 'dist', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fa', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*.js'), os.path.join('static', 'bootstrap-combobox', 'css', '*.css'), os.path.join('static', 'bootstrap-combobox', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', '*.md'), os.path.join('static', 'bootstrap', 'js', '*.*'), os.path.join('static', 'bootstrap', 'css', '*.*'), os.path.join('static', 'labelauty', 'source', '*.*'), os.path.join('static', 'areyousure', '*.js'), os.path.join('static', 'popper', '*.*'), os.path.join('static', 'popper', 'umd', '*.*'), os.path.join('static', 'popper', 'esm', '*.*'), os.path.join('static', '*.html')]}
      )
