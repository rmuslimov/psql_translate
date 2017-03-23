# Install

  * Setup your google.api_key to .env file.
	```
	$ cp .example.env .env
	```
	Update `.env` with you api_key

  * Generate python functions (new `install_py.sql` should appear in root dir)
    ```
	$ make generate
	```
  * Install sql - assuming that you have `test` db.
    ```
	$ make install
	```
# Uninstall

  * Run:
    ```
	$ make uninstall
	```
