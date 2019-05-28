# Guide to create an App for Assets.BreatheCo.de

The mayority of breatheco.de functionalities are developed on `assets apps`, an `asset app` is basically a small application with a particular purpose, [these are some examples of applications](https://github.com/breatheco-de/assets/blob/master/docs/Apps.md) already published under the assets repository.

### Boilerplate

Start coding your application based on [the following boilerplate](https://github.com/4GeeksAcademy/react-hello).

### Using react-router:

Assets application are always published under the `apps` subdirectory like this:
```
https://assets.breatheco.de/apps/<your_app_name>
```
And that has to be considered if you plan to use React Router, you will have to add a basename on the Browser Router on the production version.

### Security Tokens:

If you need to communicate with the BreatheCode API's you will receive the user session tokens as Query String variables, `assets_token` and `bc_token` like this:
```
https://assets.breatheco.de/apps/your-app?assets_token=<token>& bc_token=<token2>
```
