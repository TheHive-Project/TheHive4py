#OrganisationEndpoint


####create(self, organisation)

Create a new organisation.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```organisation```  |```InputOrganisation```       |The case to create                             |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputOrganisation``` |The created org                                |      



####get(self, org_id)

Get an existing organisation.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The ID of the org to retrieve                  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputOrganisation``` |The retrieved org                              |   


####update(self, org_id, fields)

Update an organisation.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the org to update                    |required         |
|```fields```        |```InputUpdateOrganisation``` |The updated org                                |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####delete(self, org_id)

Delete an organisation.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The ID of the org to update                    |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####link(self, org_id, other_org_id, link)

Link between organisations.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The ID of the org to link                    |required         |
|```other_org_id```  |```str```                     |The ID of the org to link with               |required         |  
|```link```          |```InputOrganisationLink```   |the link between the org                       |required         |  


**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####unlink(self, org_id, other_org_id)

Unlink organisations.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The ID of the org to unlink                    |required         |
|```other_org_id```  |```str```                     |The ID of the org to unlink with               |required         |  
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####list_links(self, org_id)

List the links of the specified organisation.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The organisation's ID                          |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputOrganisation]```|A list of `OutputOrganisation` objects representing the linked orgs| 


####bulk_link(sel f, org_id, links)

Add or update multiple links for an organization.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```org_id```        |```str```                     |The ID of the organization to add or update the links for                                                                                                 |required         |
|```links```         |```List[InputBulkOrganisationLink]``` |A list of link objects to add or update                                                                                              |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


####list_sharing_profiles(self)

Retrieve a list of sharing profiles.
          
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputSharingProfile]```|A list of OutputSharingProfile objects containing information about the sharing profiles.| 


####find(self, filters, sortby, paginate)

Find organisations based on the specified filters, sort order, and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputOrganisation]```  |A list of matching cases                   | 


####count(self, filters)

Count the organisations that match the specified filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |


**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```int```                   |The number of matching orgs                    | 


