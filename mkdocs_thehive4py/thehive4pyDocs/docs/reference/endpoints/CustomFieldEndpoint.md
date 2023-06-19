#CustomFieldEndpoint

Class representing TheHive's custom field endpoint.


####create(self, custom_field)

Create a custom field.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```custom_field```  |```InputCustomField```         |An object containing the custom field data    |required         |

           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCustomField```  |An object containing the created custom field data |      



####list(self)

Gets a list of all custom fields.
          
**Returns:**

|Type                          |Description                                    
|-------------------------    |-----------------------------------------------|
|```List[OutputCustomField]```|A list of objects containing the custom field data|      


####delete(self, custom_field_id)

Deletes the specified custom field.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```custom_field_id```|```str```                    |The ID of the custom field                     |required         |

           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |   



####update(self, custom_field_id, fields)

Updates the specified custom field with the provided fields.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```custom_field_id```|```str```                    | The ID of the custom field                    |required         |
|```fields```        |```InputUpdateCustomField```  | An object containing the updated custom field data                                                                                                |required         |
      
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  
