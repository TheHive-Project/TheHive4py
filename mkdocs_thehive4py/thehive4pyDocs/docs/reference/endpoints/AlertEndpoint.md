#AlertEndpoint


#### create(self, alert, attachment_map) 

Create a new alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert```         |```InputAlert```              |The data for the new alert                     |required         |
|```attachment_map```|```Optional[Dict[str, str]]```|A dictionary mapping attachment keys to                       file path                                                                                           |Not required     |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputAlert```        |The created alert                              |      



#### get(self, alert_id)

Get an existing alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to get                     |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputAlert```        |The retrieved alert                            |   



#### update(self, alert_id, fields)

Update an existing alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to update                  |required         |
|```fields```        |```InputUpdateAlert```        |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  



#### delete(self, alert_id)

Delete an existing alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to delete                  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### bulk_update(self,fields)

Update multiple alerts at once.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```fields```        |```InputBulkUpdateAlert```    |The updates to apply                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### bulk_delete(self, ids)

Delete multiple alerts at once.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```ids```           |```List[str]```               |The IDs of the alerts to delete                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### follow(self, alert_id)

Follow an alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to follow                  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### unfollow(self, alert_id)

Unfollow an alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to unfollow                |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### promote_to_case(self, alert_id, fields)

Promote an alert to a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to promote                 |required         |
|```fields```        |```InputPromoteAlert```       |The fields to include in the new case          |required         |
           
**Returns:**

|Type                       |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The newly created case                         |  


#### create_observable(self, alert_id, observable, observable_path)

Create an observable.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to associate the observable with                                                                                                |required         |
|```observable```    |```InputObservable```         |The observable to create                       |required         |
|```observable_path```|```Optional[str]```          |The path to associate with the observable. Default: ```None```                                                                                          |Not         required         |

           
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputObservable]```|The created observable                         |  



#### merge_into_case(self, alert, case_id)

Merge an alert into a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to merge into the case     |required         |
|```case_id```       |```str```|The ID of the case to merge the alert into                          |required         |
           
**Returns:**

|Type                        |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The updated case                               |  


#### bulk_merge_into_case(self, case_id, alert_ids)

Bulk merge alerts into a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to merge the alerts into    |required         |
|```alert_ids```     |```List[str]```               |The IDs of the alerts to merge                 |required         |
           
**Returns:**

|Type                       |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The updated case                               |  


#### find(self, filters, sortby, paginate)

Find alerts matching the given filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
|```sortby```        |```Optional[SortExpr]```      | The sorting criteria to apply to the search   |required         |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |required         |
        
**Returns:**

|Type                          |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputAlert]```     |The matching alerts                            | 


#### count(self, filters)

Count alerts matching the given filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
           
**Returns:**

|Type                        |Description                                    
|-------------------------|-----------------------------------------------|
|```int```                |The number of matching alerts                  |  


#### find_observables(self, alert_id, filters, sortby, paginate)

Find observables matching the given filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to retrieve observables for|required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
|```sortby```        |```Optional[SortExpr]```      |The sorting criteria to apply to the search    |required         |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |required         |
        
**Returns:**

|Type                           |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputObservable]```|The matching observables                       | 


#### find_comments(self, alert_id, filters, sortby, paginate)

Retrieve comments for a given alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to retrieve comments for   |required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |None             |
|```sortby```        |```Optional[SortExpr]```      |The sorting criteria to apply to the search    |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |None             |
        
**Returns:**

|Type                          |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputComment]```   |A list of comments for the given alert         | 


#### create_procedure(self, alert_id, procedure)

Create a procedure for a given alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to create the procedure for|required         |
|```procedure```     |```InputProcedure```          |The procedure to create                        |required         |
           
**Returns:**

|Type                       |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The newly created case                         |  


#### find_procedure(self, alert_id, filters, sortby, paginate)

Retrieve procedure for a given alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to retrieve procedures for |required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |None             |
|```sortby```        |```Optional[SortExpr]```      |The sorting criteria to apply to the search    |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |None             |
        
**Returns:**

|Type                          |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputProcedure]``` |A list of procedures for the given alert       | 