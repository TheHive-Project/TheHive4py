#CaseEndpoint

**CaseId: Union[str, int]**

#### create(self, case)

Create a new case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case```          |```InputCase```               |The case to create                             |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The created case                             |      



#### get(self, case_id)

Get an existing case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to retrieve                 |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The retrieved case                           |   



#### delete(self, case_id)

Delete an existing case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to delete                  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  



#### update(self, case_id, case)

Update an existing case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to update                   |required         |
|```case```          |```InputUpdateCase```         |The updated case                               |required         |

           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### bulk_update(self,fields)

Update multiple cases at once.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```fields```        |```InputBulkUpdateCase```     |The updates to apply                           |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### merge(self, case_ids)

Merge multiple cases at once.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_ids```      |```Sequence[CaseId]```        |The IDs of the cases to merge                  |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```OutputCase```         |The merged case                                |  


#### unlink_alert(self, case_id, alert_id)

Remove a link between a case and an alert.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to unlink the alert from    |required         |
|```alert_id```      |```str```                     |The ID of the alert to unlink from the case    |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### merge_similar_observables(self, case_id)

Merge similar observables in a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to merge similar observables in                                                                                                  |required         |
           
**Returns:**

|Type                     |Description                                    
|-------------------------|-----------------------------------------------|
|```dict```               |A dictionary containing information about the merged observables |  


#### get_linked_cases(self, case_id)

Get a list of cases linked to the specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to get linked cases for     |required         |

**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputCase]```   |A list of OutputCase objects representing the linked cases|  


#### delete_custom_field(self, custom_field_id)

Delete a custom field.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```custom_field_id```|```str```                    |The ID of the custom field to delete           |required         |

**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |                                               |  



#### import_from_file(self, import_case, import_path)

Import a case from a file.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```import_case```   |```InputImportCase```         |The ID of the alert to merge into the case     |required         |
|```import_path```   |```str```                      |The ID of the case to merge the alert into    |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```dict```               |A dictionary containing information about the imported case|  


#### export_to_file(self, case_id, password, export_path)

Export a case to a file.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to export                   |required         |
|```password```      |```str```                     |The password to encrypt the exported file with |required         |
|```export_path```   |```str```                     |The path to save the exported file to          |required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```None```               |                                               |  


#### get_timeline(self, case_id)

Retrieve the timeline of a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case                             |required         |

        
**Returns:**

|Type                         |Description                                    |
|-------------------------   |-----------------------------------------------|
|```OutputTimeline```        |The timeline of the case                       | 


#### add_attachment(self, case_id, attachment_paths)

Add one or more attachments to a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to add the attachments to   |required         |
|```attachment_paths```|```List[str]```             |A list of file paths for the attachments to add|required         |

           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputAttachment]```|A list of OutputAttachment objects representing the added attachments                 |  


#### download_attachment(self, case_id, attachment_id, attachment_paths)

Download an attachment from a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The case's id                                  |required         |
|```attachment_id``` |```str```                     |The attachment's id                            |required         |
|```attachment_paths```|```str```                   |The attachment's path                          |required         |
        
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |                                               | 


#### delete_attachment(self, case_id, attachment_id)

Delete an attachment from a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The case's id                                  |required         |
|```attachment_id``` |```str```                     |The attachment's id                            |required          |

        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |                                               | 


#### list_shares(self, case_id)

List the shares of the specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to list the shares of       |required         |
           
**Returns:**

|Type                      |Description                                    
|-------------------------|-----------------------------------------------|
|```List[OutputShare]```  |A list of `OutputShare` objects representing the shares of the specified case|  


#### share(self, case_id, shares)

Share a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to share                    |required         |
|```shares```        |```List[InputShare]```        |A list of `InputShare` objects representing the organisations to share the case with                                                                                           |required         |

        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputShare]```     |A list of `OutputShare` objects representing the shares that were created by the operation| 


#### unshare(self, case_id, organisation_ids)

Unshare a case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to unshare                  |required         |
|```organisation_ids```|```List[str]```             |A list of organisation IDs representing the organisations to unshare the case from                                                                                           |required         |

        
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |A list of `OutputShare` objects representing the shares that were created by the operation| 


#### set_share(self, case_id, shares)

Set a share.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to set the shares of        |required         |
|```shares```        |```List[InputShare]```        | A list of `InputShare` objects representing the organisations to share the case with                                                                                           |required         |

        
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputShare]```     |A list of `OutputShare` objects representing the shares that were created| 


#### remove_share(self, share_id)

Remove the specified share.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```share_id```      |```str```                     |The ID of the share to remove                  |required         |

        
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |       | 


#### update_share(self, share_id, profile)

Update the profile of a shared case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```share_id```      |```str```                     |The ID of the share to update                  |required         |
|```profile```       |```str```                     |The new profile to set                         |required         |

        
**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```None```                  |       | 


#### find(self, filters, sortby, paginate)

Find cases based on the specified filters, sort order, and pagination.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

        
**Returns:**

|Type                       |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputCase]```      |A list of matching cases                       | 


#### count(self, filters)

Count cases based on the specified filters.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query                 |None             |


**Returns:**

|Type                        |Description                                    
|-------------------------   |-----------------------------------------------|
|```List[OutputCase]```      |A list of matching cases                       | 


#### create_task(self, case_id, task)

Create a task in a specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to create the task for      |required         |
|```task```          |```InputTask```               |The task to create                             |required         |
       
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```OutputTask```            |The created task                               | 


#### find_tasks(self, case_id, filters, sortby, paginate)

Find tasks in a specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to search for tasks in      |required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |
      
**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputTask]```      |A list of tasks associated with the specified case| 


#### create_observable(self, case_id, observable, observable_path)

Create one or more observables associated with the specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to create observables for   |required         |
|```observable```    |```InputObservable]```        |The observable to create                       |required         |
|```observable_path```|```Optional[str]```          |Optional path to a file containing additional data related to the observable                                                                                          |None             |
    
**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputObservable]```|A list of observables that were created           | 


#### find_observables(self, case_id, filters, sortby, paginate)

Find observables associated with the specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to search for observables in|required         |
|```filters```       |```Optional[FilterExpr]```    |The filters to apply to the query              |None             |
|```sortby```        |```Optional[SortExpr]```      |The sort order to apply to the results         |None             |
|```paginate```      |```Optional[Paginate]```      |The pagination parameters to apply to the query|None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputObservable]```|A list of observables associated with the specified case| 


#### create_procedure(self, case_id, procedure)

Create a new procedure associated with the specified case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to create the procedure for |required         |
|```procedure```     |```InputProcedure```          |The procedure to create                        |required         |
       
**Returns:**

|Type                         |Description                                    
|-------------------------   |-----------------------------------------------|
|```OutputProcedure```       |The procedure that was created                 | 


#### find_procedures(self, case_id, filters, sortby, paginate)

Finds procedures associated with a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to search for procedures    |required         |
|```filters```       |```Optional[FilterExpr]```    |A filter expression to filter the procedures by|None             |
|```sortby```        |```Optional[SortExpr]```      |A sort expression to sort the procedures by    |None             |
|```paginate```      |```Optional[Paginate]```      |A pagination object to limit and offset the results                                                                                             |None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputProcedure]``` |A list of procedures associated with the given case| 


#### find_attachments(self, case_id, filters, sortby, paginate)

Finds attachments associated with a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to search for attachments   |required         |
|```filters```       |```Optional[FilterExpr]```    |A filter expression to filter the attachments by|None             |
|```sortby```        |```Optional[SortExpr]```      |A sort expression to sort the attachments by   |None             |
|```paginate```      |```Optional[Paginate]```      |A pagination object to limit and offset the results                                                                                             |None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputAttachment]```|A list of attachments associated with the given case| 


#### find_comments(self, case_id, filters, sortby, paginate)

Finds comments associated with a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```str```                     |The ID of the case to search for comments      |required         |
|```filters```       |```Optional[FilterExpr]```    |A filter expression to filter the comments by  |None             |
|```sortby```        |```Optional[SortExpr]```      |A sort expression to sort the comments by      |None             |
|```paginate```      |```Optional[Paginate]```      |A pagination object to limit and offset the results                                                                                             |None             |

**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```List[OutputComment]```   |A list of comments associated with the given case | 


#### close(self, case_id, status, summary, impact_status)

Close a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to close                    |required         |
|```status```        |```CaseStatusValue```         |The status of the case after closing           |required         |
|```summary```       |```str```                     |A summary of the case                          |required         |
|```impact_status```      |```ImpactStatusValue```  |The impact status of the case after closing    |"NotApplicable"  |
 
**Returns:**

|Type                         |Description                                    
|-------------------------   |--------------------------------------------------|
|```None```                  |                                                  | 


#### open(self, case_id, status, summary, impact_status)

Open a given case.

**Parameters:**

|Name                |Type                          |Description                                    |Default|
|--------------------|------------------------------|-----------------------------------------------|-----------------|
|```case_id```       |```CaseId```                  |The ID of the case to open                     |required         |
|```status```        |```CaseStatusValue```         |The status of the case after opening. Default is CaseStatus.InProgress                                                                                       |CaseStatus.InProgress|


**Returns:**

|Type                        |Description                                    
|-------------------------   |--------------------------------------------------|
|```None```                  |                                                  | 