#ProcedureEndpoint


####create_in_alert(self, alert_id, procedure)

Create a procedure for a given alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID or name of the alert to create the procedure for |required         |
|```procedure```     |```InputProcedure```          |The procedure to create                        |required     |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputProcedure```    |The created procedure                          |      


####create_in_case(self, case_id, procedure)

Create a procedure for a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```      |```str```                     |The ID or name of the case to create the procedure for |required         |
|```procedure```     |```InputProcedure```          |The procedure to create                        |required     |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputProcedure```    |The created procedure                          |   


####get(self, procedure_id)

Retrieves a procedure.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```procedure_id```  |```str```                     |The ID of the procedure to get                 |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputProcedure```    |The retrieved procedure                        |   


####delete(self, procedure_id)

Delete an existing procedure.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```procedure_id```  |```str```                     |The ID of the procedure to delete              |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####update(self, procedure_id, fields)

Update an existing procedure.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```procedure_id```  |```str```                     |The ID of the procedure to update              |required         |
|```fields```        |```InputUpdateProcedure```    |The fields to update                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####find(self, filters, sortby, paginate)

Finds procedures based on filters, sort experssions and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the search             |required         |
|```sortby```        |```Optional[SortExpr]```      | The sorting criteria to apply to the search   |required         |
|```paginate```      |```Optional[Paginate]```      |The pagination settings to apply to the search |required         |
        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputProcedure]``` |A list of procedures associated with the given case| 


