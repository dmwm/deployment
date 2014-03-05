### DAS deployment procedure

DAS follows standard cmsweb deployment procedure. It has deploy script which
installs new DAS release along with DAS maps (they're part of DAS release).
But DAS maps can be updated within some DAS release. Therefore we provide
instructions how to start-up DAS either from fresh RPMs or once new DAS maps
will be deployed and uploaded.

#### Scenario A:

under this scenario we assume that DAS code and DAS maps are provided in RPMS.
Therefore to start DAS service we only need to perform the following action:
```manage start "I did read documentation"```
This action will deploy DAS maps into stageing area from DAS release area. A
new file *das_maps_status* will be created with appropriate message and
timestamp.

#### Scenario B:

under this scenario we have installed DAS release, but would like to update DAS
maps. To do so we need to perform the following actions:

- stop DAS service
  ```manage stop "I did read documentation"```
- fetch new DAS maps
  ```manage fetchmaps "I did read documentation"```
  a *das_maps_status* file will be updated with appropriate message and
  timstamp; DAS service will not be affected by this action (if it is running
  it will continue); DAS service it will not reload maps, this should done
  explicitly via updatemaps action
- upload new DAS maps into MongoDB
  ```managa udatemaps "I did read documentation"```
  a *das_maps_status* file will be updated with appropriate message and
  timstamp; DAS service will be stopped during this action and will need to be
  restarted afterwards
- start DAS service
  ```manage start "I did read documentation"```
  will stop and start DAS service
