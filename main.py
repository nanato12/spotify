from spotify.credential_server import HOST, PORT, app

SERVER = True

if SERVER:
    app.run(host=HOST, port=PORT)
