# edge_inference

### List of Commands

1) Set up the bridge network
```
./network_create.sh
```

2) Set up the **inference** container

a) This was in the repo
```
./inference.sh
```

b) This one is an alternate that also works.
```
sudo ./inference2.sh

docker exec -it inference bash
```

3) Set up the **broker** container
```
docker build -t broker -f Dockerfile.localbroker .

docker run -d --name broker --network car -p 1883:1883 --hostname broker broker
```

4) Set up **car** container
```
docker build -t car -f Dockerfile.car .

docker run -d --name car --network car --hostname car car /bin/sh
```
- Run the below command if you do not exec into the container.
```
docker exec -it car /bin/sh
```

5) Run car_class python script in **car** container
```
python3 car_class.py
```

6) Run inference python script in **inference** container
```
python3 inference.py
```


