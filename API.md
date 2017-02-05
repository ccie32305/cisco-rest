# API documentation

**Enable Interace**
----
  Returns json data of switchname and port.

* **URL**

  /api/v1/interfaceenable/\<switchname\>/\<interface\>/\<port\>
  
  /api/v1/interfaceenable/\<switchname\>/\<interface\>/\<submodule\>/\<port\>
  

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "success" : "deswitch01/GigabitEthernet0/1" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "error" : "system could not be reached }`


* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/api/v1/interfaceenable/deswitch01/GigabitEthernet0/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
