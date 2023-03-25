## Chart Editor

This example is a simple chart editor that relies on the [vegafusion-wasm](https://www.npmjs.com/package/vegafusion-wasm) and [vegafusion-embed](https://www.npmjs.com/package/vegafusion-embed) packages, and connects to an instance of the VegaFusion Server over gRPC-Web.

### Setup

#### Download VegaFusion Server
Download and unzip a vegafusion-server instance for your operating system from VegaFusion's [GitHub Releases](https://github.com/hex-inc/vegafusion/releases). One of:
 - `vegafusion-server-linux-64.zip` 
 - `vegafusion-server-osx-64.zip` 
 - `vegafusion-server-osx-arm64.zip` 
 - `vegafusion-server-win-64.zip`

For best results, make sure the version of `vegafusion-server` matches the versions of `vegafusion-wasm` and `vegafusion-embed` in `apps/vegafusion-editor-grpc-web/package.json`.

#### Run VegaFusion Server in gRPC-Web mode

Launch VegaFusion Server on port 50051 with the `--web` flag to enable gRPC-Web support:
```
./vegafusion-server --port 50051 --web
```

#### Build and run editor app
Build and launch editor with
```
npm install
npm run start
```

Then open the app at http://localhost:8080/

![VegaFusion Editor Demo](https://user-images.githubusercontent.com/15064365/227670166-6364e5ce-fb31-4964-8603-e77201a54ebe.png)
