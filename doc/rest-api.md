Sensor Network API
==================

Overview
--------

Each API request requires a user API key. The key is the first element of the URL.

For example, the full URL for a request for the WSN catalog (Section 1.1) is:

    https://hostname.domain.tld/api/<API KEY>/wsns

For brevity the above URL will be abbreviated throughout this document as:

    <API-BASE>/wsns

--------------------------------------------------------------------------------
1. Operations on Wireless Sensor Network Objects
================================================

1.1. Get catalog of all public Wireless Sensor Networks
-------------------------------------------------------
**Description:**

This returns only networks a user has read access to. This includes networks a user has access to, and any declared public networks.

**URL:**

    GET <API-BASE>/wsn

**BODY:**

Ignored.

**Returns:**

    [
      {<WSN Object>},
      {<WSN Object>},
      ...
      {<WSN Object>}
    ]

1.2. Get information about a specific Wireless Sensor Network
-------------------------------------------------------------
**Description:**

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>

**BODY:**

Ignored.

**Returns:**

    { "name" : "CMSC 668 Project",
      "id" : <WSN_ID>,
      "api-key" : <API_KEY>,
      "owner-name" : "Mark Gray",
      "owner-email" : "mgray2@umbc.edu",
      "owner-phone" : "1-800-555-1234",
      "gps-latitude" : "39.51N",
      "gps-longitude" : "76.36W",
      "gps-altitude" : "331"
    }

1.3. Create New Wireless Sensor Network
---------------------------------------
**Description:**

**URL:**

    POST <API-BASE>/wsn

**BODY:**

    { "name" : "CMSC 668 Project",
      "public" : true,
      "owner-name" : "Mark Gray",
      "owner-email" : "mgray2@umbc.edu",
      "gps-latitude" : "39.51N",
      "gps-longitude" : "76.36W",
      "gps-altitude" : "331"
    }

**RETURNS:**

    { "id" : "0e901111-a281-4dce-8478-1a996cee5a9b" }

1.4. Update Existing Wireless Sensor Network
--------------------------------------------
**Description:**

The body of this request may contain as many or as few data elements present in the WSN object.
The data elements of the wsn object will be updated with the new values.

**URL:**

    PUT <API-BASE>/wsn/<WSN_ID>

**BODY:**

    { "name" : "CMSC 668 Final Project",
      "public" : false
    }

**RETURNS:**

    {}

1.5 Remove a Wireless Sensor Network
------------------------------------
**Description:**

This action is final and cannot be undone. It will remove the WSN and all sensors and channels it contains. This action **WILL** remove the data associated with this WSN.

**URL:**

    DELETE <API-BASE>/wsn/<WSN_ID>

**BODY:**

Ignored.

**RETURNS:**

    {}

--------------------------------------------------------------------------------
2 Operations on Sensor Objects
==============================

2.1 Add New Sensor
------------------
**Description:**

**URL:**

    POST https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors

**BODY:**
    
    { "name" : "Sensor #88",
      "loc-x" : 5,
      "loc-y" : 5,
      "loc-z" : 5,
      "unit" : "feet",
      "sample-frequency" : 4,
      "sample-interval" : "hour" }

2.2 Get Sensor
--------------
**Description:**

**URL:**

    GET https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>

**RETURNS:**

    { "name" : "Sensor #88",
      "loc-x" : 5,
      "loc-y" : 5,
      "loc-z" : 5,
      "unit" : "feet",
      "sample-frequency" : 4,
      "sample-interval" : "hour",
      "channels" : [ <channel_A_object>, <channel_B_object>, ... ] }

2.3 Update Existing Sensor
--------------------------
**Description:**

**URL:**

    PUT https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>

**BODY:**

    { "name" : "Side Temperature",
      "sample-frequency" : 15 }

2.4 Delete Sensor
-----------------
**Description:**

**URL:**

    DELETE https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>

--------------------------------------------------------------------------------
3. Operations on Sensor Channels
================================

3.1 Add New Channel
-------------------
**Description:**

**URL:**

    POST https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels

**BODY:**

    { "name" : "Front IR",
      "type" : "temperature",
      "units" : "C" }

3.2 Get Channel
---------------
**Description:**

**URL:**

    GET https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

**RETURNS:**

    { "name" : "Front IR",
      "id" : <Channel ID>,
      "type" : "temperature",
      "units" : "C" }

3.3 Update Existing Channel
---------------------------
**Description:**

**URL:**

    PUT https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

**BODY:**

    { "units" : "F"}

3.4 Delete Channel
------------------
**Description:**

**URL:**

    DELETE https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

--------------------------------------------------------------------------------
4 Operations on Sample Objects
==============================

4.1 Add a New Data Record
-------------------------
**Description:**

**URL:**

    POST https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/data

**BODY:**

    { "key" : <WSN_API_KEY>,
      "datetime" : "20131023T0502Z" # Use ISO-8601 Format ONLY
      "data" : { "<CHANNEL_ID>" : 5,
                 "<CHANNEL_ID" : 10 }
    }

4.2 View data records
---------------------
**Description:** TODO: This is critical and isn't defined yet...

**URL:**

    GET https://<HOSTNAME BASE>/api/wsn/<WSN_ID>/data

**RETURN:**

