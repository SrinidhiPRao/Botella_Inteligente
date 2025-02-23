## Status

- Sensor data ingress code completed.
- Docker has been setup.
- time series database has been setup.
- Docker connection to local machine established.
- Setup backend in container
- Setup frontend in container
- Modularise the code

## ToDo

- Stop fetcher from crashing. It should retry instead.

# Instructions to Run

- For testing without Arduino.

```
    uvicorn external.faux_sensor:app --host 0.0.0.0 --port 5000 --reload
```

- While Arduino is connected.

```
    uvicorn external.sensor:app --host 0.0.0.0 --port 5000 --reload
```

- Run the Application.

```
    docker compose up --build -d
```

- Stopping the Application.

```
    docker compose down --remove-orphans
```
