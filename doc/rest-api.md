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
2. Operations on Sensor Objects
===============================

2.1. Get list of sensors in a WSN
---------------------------------
**Description:**

Returns a list of all sensors in a specific Wireless Sensor Network.

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>/sensors

**BODY:**

Ignored.

**RETURNS:**

    [ {<Sensor Object>},
      {<Sensor Object>},
      ...
      {<Sensor Object>},
    ]

2.2. Get information about a specific Sensor
--------------------------------------------
**Description:**

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>

**BODY:**

Ignored.

**RETURNS:**

    { "name" : "Sensor #88",
      "id" : "98f07253-ea74-4c1a-aef3-27657563f8d7"
      "loc-x" : 5,
      "loc-y" : 5,
      "loc-z" : 5,
      "unit" : "feet",
      "sample-frequency" : 4,
      "sample-interval" : "hour",
      "channels" : [ <channel_A_object>, <channel_B_object>, ... ]
    }

2.3. Add New Sensor to a WSN
----------------------------
**Description:**

**URL:**

    POST <API-BASE>/wsn/<WSN_ID>/sensors

**BODY:**

    { "name" : "Sensor #88",
      "loc-x" : 5,
      "loc-y" : 5,
      "loc-z" : 5,
      "unit" : "feet",
      "sample-frequency" : 4,
      "sample-interval" : "hour"
    }

**RETURNS:**

    { "id" : "98f07253-ea74-4c1a-aef3-27657563f8d7" }

2.4. Update Existing Sensor
---------------------------
**Description:**

The body of this request may contain as many or as few data elements present in the Sensor object.
The data elements of the sensor will be updated with the new values.

**URL:**

    PUT <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>

**BODY:**

    { "name" : "Side Temperature",
      "sample-frequency" : 15 }

**RETURNS:**

    {}

2.5. Remove Sensor from a WSN
-----------------------------
**Description:**

This action is final and cannot be undone. It will remove this sensor and all channels it contains. Data collected by this sensor will **NOT** be removed.

**URL:**

    DELETE <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>

**BODY:**

Ignored.

**RETURNS:**

    {}

--------------------------------------------------------------------------------
3. Operations on Sensor Channels
================================

3.1. Get list of Channels in a Sensor
-------------------------------------
**Description:**

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels

**BODY:**

    [ {<Channel Object},
      {<Channel Object},
      ...
      {<Channel Object>}
    ]

**RETURNS:**

    {}

3.2. Get information about a specific Channel
---------------------------------------------
**Description:**

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

**RETURNS:**

    { "name" : "Front IR",
      "id" : <Channel ID>,
      "type" : "temperature",
      "units" : "C"
    }

**RETURNS:**

    {}

3.3. Add New Channel to Sensor
------------------------------
**Description:**

**URL:**

    POST <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels

**BODY:**

    { "name" : "Front IR",
      "type" : "temperature",
      "units" : "C"
    }

**RETURNS:**

    { "id" : "62408acd-893f-4f74-8c85-5ff793e3f475" }

3.4. Update Existing Channel
----------------------------
**Description:**

The body of this request may contain as many or as few data elements present in the Channel object.
The data elements of the channel will be updated with the new values.

**URL:**

    PUT <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

**BODY:**

    { "units" : "F"}

**RETURNS:**

    {}

3.5. Remove Channel from Sensor
-------------------------------
**Description:**

This action is final and cannot be undone. It will remove this channel. Any data already collected by this sensor will **NOT** be removed.

**URL:**

    DELETE <API-BASE>/wsn/<WSN_ID>/sensors/<SENSOR_ID>/channels/<CHANNEL_ID>

**BODY:**

Ignored.

**RETURNS:**

    {}

--------------------------------------------------------------------------------
4. Operations on Data Samples
==============================

4.1. Add a New Data Record
--------------------------
**Description:**

This API endpoint is used by WSN servers to upload new sensor data as it is being collected.

The datetime field is used to specify when the data was collected. This field is optional. If omitted, the WSN service will use the time when the request was made.

**URL:**

    POST <API-BASE>/wsn/<WSN_ID>/data

**BODY:**

    { "datetime" : "20131023T0502Z" # ISO-8601 Format and UNIX datetime are both supported.
      "data" : [ { "sensor_id" : "98f07253-ea74-4c1a-aef3-27657563f8d7"
                   "data" : { "<CHANNEL_ID>" : 5,
                              "<CHANNEL_ID>" : 10 }
                 },
                 { "sensor_id" : "98db944c-b906-4bc5-bcb8-0e237c0fd079"
                   "data" : { "<CHANNEL_ID>" : 5,
                              "<CHANNEL_ID>" : 10 }
                 }
               ]
    }

4.2. View Data Records
----------------------
**Description:**

Provide an extensible interface to request raw and processed data from a Wireless Sensor Network.

This endpoint has three modes: live, historical, and processed.

* **Live:** Return the most recent values for every sensor/channel within this WSN.
* **Historical:** Return recorded data from sensors selected by sensor, channel, or start/end time boundary.
* **Processed** Return the results of a data processing job.

**URL:**

    GET <API-BASE>/wsn/<WSN_ID>/data

**HTTP QUERY PARAMETERS:**

    "mode" : { "live", "historical", "processed" }

If the mode is "historical" or "processed" the following additional parameters are available:

    "startdate" : <datetime> # ISO-8601 Format only
    "enddate" : <datetime>
    "sensors" : <sensor id>[,<sensor id>, ...]

**RETURN:**

    { "data" : [ { "datetime" : "20131023T0502Z" # ISO-8601 Format
                   "sensor_id" : "98f07253-ea74-4c1a-aef3-27657563f8d7"
                   "data" : { "<CHANNEL_ID>" : 5,
                              "<CHANNEL_ID>" : 10 }
                 },
                 { "sensor_id" : "98db944c-b906-4bc5-bcb8-0e237c0fd079"
                   "data" : { "<CHANNEL_ID>" : 5,
                              "<CHANNEL_ID>" : 10 }
                 }
               ]
    }

