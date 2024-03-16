#ObservableEndpoint

Class representing TheHive's observable endpoint.


####create_in_alert(self, alert_id, observable, observable_path)

Create a new observable in an alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```alert_id```      |```str```                     |The ID of the alert to create the observable within                                                                                              |required         |
|```observable```    |```InputObservable```         |The observable to create                       |required         |
|```observable_path```|```Optional[str]```          |The path to the observable file (if it's a file)|None         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputObservable]```|A list containing the created observable |      


####create_in_case(self, case_id, observable, observable_path)

Create a new observable in a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```      |```str```                     |The ID of the case to create the observable within                                                                                              |required         |
|```observable```    |```InputObservable```         |The observable to create                       |required         |
|```observable_path```|```Optional[str]```          |The path to the observable file (if it's a file)|None         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputObservable]```|A list containing the created observable |   



####get(self, observable_id)

Get the specified observable.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable to retrieve           |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputObservable```   |An object containing the observable data |  

  

####delete(self, observable_id)

Delete the specified observable.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable to delete             |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   


####update(self, observable_id, fields)

Update the specified observable.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable to update             |required         |
|```fields```        |```InputUpdateObservable```   |The fields to update                           |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   


####bulk_update(self, fields)

Update multiple observables at once.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```fields```        |```InputBulkUpdateObservable```|he fields to update for the observables       |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   


####share(self, observable_id, organisations)

Share an observable with a list of organisations.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable to share              |required         |
|```organisations``` |```List[str]```               |The list of organisations to share the observable with                                                                                                |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   


####unshare(self, observable_id, organisations)

Unshare an observable with a list of organisations.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable to unshare            |required         |
|```organisations``` |```List[str]```               |The list of organisations to unshare the observable with                                                                                                |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####list_shares(self, observable_id)

List the organisations an observable is shared with.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable           |required         |
          
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputShare]```  |A list of share objects for the observable     |  


####find(self, filters, sortby, paginate)

Gets a list of observables based on the provided filters, sort expression, and pagination parameters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

       
**Returns:**

|Type                             |Description                                    
|-------------------------       |-----------------------------------------------|
|```List[OutputObservable]```    |A list of observables matching the specified criteria | 


####count(self, filters)

Count the number of observables matching the specified criteria.
**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
       
**Returns:**

|Type                             |Description                                    
|-------------------------       |-----------------------------------------------|
|```int```                       |The number of observables matching the specified criteria | 


####download_attachment(self, observable_id, attachment_id, observable_path, as_zip)

Download an attachment that belong to an observable.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_id``` |```str```                     |The ID of the observable that the attachment belongs to                                                                                                  |required         |
|```attachment_id``` |```str```                     |The ID of the attachment to download           |required         |
|```observable_path```|```str```                    |The path to save the downloaded attachment to  |required         |
|```as_zip```        |```str```                     |If True, downloads the attachment as a zip file|False            |
      
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               | 