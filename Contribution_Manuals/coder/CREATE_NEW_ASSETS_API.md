### Steps to create a new API

We have prepared this is the ideal boilerplate to start coding, please clone the repo or opened in Gitpod (recomended)  
https://github.com/breatheco-de/assets-api-hello

Here is an example of your routes.php file:

```php
 use Psr\Http\Message\ServerRequestInterface as Request;
 use Psr\Http\Message\ResponseInterface as Response;
 
return function($api){
 
/**
* This is an example endpoint that matches the following URL:
* GET: /apis/<your_api_name_slug>/all
*/
	$api->get('/all', function (Request $request, Response $response, array $args) use ($api) {
	    //any php logic for your function
	});

	//add here any other endpoints you want

	return $api;
}
```
