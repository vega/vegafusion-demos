## Chart Editor

This example is a simple chart editor that relies on the [vegafusion-wasm](https://www.npmjs.com/package/vegafusion-wasm) and [vegafusion-embed](https://www.npmjs.com/package/vegafusion-embed) packages. It connects to an instance of the VegaFusion Server over gRPC-Web. The app is served using Flask, and custom Python logic in the Flask app is used to download a sample dataset (`datasets/flights_200k.feather`) that may be referenced in Vega specifications.

### Setup

#### Download VegaFusion Server
Download and unzip a vegafusion-server instance for your operating system from VegaFusion's [GitHub Releases](https://github.com/hex-inc/vegafusion/releases). One of:
 - `vegafusion-server-linux-64.zip` 
 - `vegafusion-server-osx-64.zip` 
 - `vegafusion-server-osx-arm64.zip` 
 - `vegafusion-server-win-64.zip`

For best results, make sure the version of `vegafusion-server` matches the versions of `vegafusion-wasm` and `vegafusion-embed` in `apps/vegafusion-editor-grpc-web/package.json`.

#### Setup Python environment
Set up a Python environment (conda or virtualenv) for the app and install the following packages

```
pip install flask pandas vegafusion
```

#### Build the client app
Build the client app with
```
npm install
npm run build
```

This will populate a `dist/` folder, which will be served by Flask. 

During development, you can use `npm run watch` instead to build the client in watch mode so that changes are automatically built.

#### Run VegaFusion Server in gRPC-Web mode

Launch VegaFusion Server on port 50051 with the `--web` flag to enable gRPC-Web support:
```
./vegafusion-server --port 50051 --web
```

#### Run the Flask server
Serve the app with the Flask development server using:

```
python app.py
```

The app will create a `datasets/` directory and download example datasets as feather files. Then it will serve the app from the `dist/` directory using Flask.

#### Open the app
Finally, open the app at http://localhost:8087/

![VegaFusion Editor Demo](https://user-images.githubusercontent.com/15064365/227670166-6364e5ce-fb31-4964-8603-e77201a54ebe.png)

### Production deployment
Here are a few things to consider when deploying an app like this demo in a production environment

#### Use a production WSGI server
Rather than the Flask development server, a production-grade WSGI server should be used. One popular example is [Gunicorn](https://docs.gunicorn.org/en/stable/).  Among other advantages, this makes it possible to have multiple workers serving the app. In this case, instead of serving the Flask app with:

```
python app.py
```

It would be served with

```
gunicorn --workers=2 app:app
```

#### Use a production proxy for gRPC-Web support
The `--web` flag to VegaFusion server is very convenient during development, but it does not support any form of authentication and so it's not the best choice for a production use case. The recommended approach to handle load-balancing and authentication is to use the [Envoy proxy](https://www.envoyproxy.io/) to convert gRPC-Web requests into standard gRPC requests. See the [Configure the Envoy Proxy](https://grpc.io/docs/platforms/web/basics/#configure-the-envoy-proxy) section of the gRPC-Web documentation.

In this configuration, the `--web` flag would not be passed to `vegafusion-server` at startup.
