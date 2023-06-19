#TimelineEndpoint

####get(self, case_id)

Retrieves the timeline for a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case                             |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputTimeline```     |The retrieved procedure                        |   


####create_event(self, case_id, event)

Creates a new event.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID or name of the case to create the event for |required     |
|```event```         |```InputCustomEvent```        |The event to create                            |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCustomEvent```  |The created event                              |      


####delete_event(self, event_id)

Deletes a specified event.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```event_id```      |```str```                     |The ID of the event                            |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update_event(self, event_id, fields)

Update an existing event.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```event_id```       |```str```                     |The ID of the event to update                  |required         |
|```fields```        |```InputUpdateCustomEvent```  |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


