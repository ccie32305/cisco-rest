# API documentation

**Enable Interface**
----
  Enable interace. Returns json data of switchname and port.

* **URL**

  /api/v1/interface-enable/\<switchname\>/\<interface\>/\<port\>
  
  /api/v1/interface-enable/\<switchname\>/\<interface\>/\<submodule\>/\<port\>
  

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"success": {"SwitchA" : "GigabitEthernet1/0/3"}}`
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `{ "error" : "system could not be reached" }`


* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/api/v1/interface-enable/deswitch01/GigabitEthernet0/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

**Shutdown Interface**
----
  Shutdown interface. Returns json data of switchname and port.

* **URL**

  /api/v1/interface-shutdown/\<switchname\>/\<interface\>/\<port\>
  
  /api/v1/interface-shutdown/\<switchname\>/\<interface\>/\<submodule\>/\<port\>
  

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"success": {"SwitchA" : "GigabitEthernet1/0/3"}}`
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `{ "error" : "system could not be reached" }`


* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/api/v1/interface-shutdown/deswitch01/GigabitEthernet0/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

