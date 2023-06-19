#ObservableTypeEndpoint

Class representing TheHive's observable type endpoint.


####create(self, observable_type)

Creates a new observable type

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_type```|```InputObservableType```    |An object containing the observable type data  |required         |

           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputObservableType```|An object containing the created observable type data |      


####get(self, observable_type_id)

Gets the specified observable type

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_type```|```str```                    |The ID of the observable type                  |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputObservableType```|An object containing the observable type data |  

  

####delete(self, observable_type_id)

Deletes the specified observable type.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```observable_type_id```|```str```                 |The ID of the observable type                  |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   



####find(self, filters, sortby, paginate)

Gets a list of observable types based on the provided filters, sort expression, and pagination parameters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

        
**Returns:**

|Type                             |Description                                    
|-------------------------       |-----------------------------------------------|
|```List[OutputObservableType]```|A list of objects containing the observable type data  | 
