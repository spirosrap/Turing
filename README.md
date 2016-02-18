Turing
======

Universal Turing machine simulator in python.As I was reading carefully Turing's seminal paper I created a simulator for a Turing machine based on the exact description of Turing's paper. Most simulators don't follow the exact same instructions Turing gave but a simplified version of it.

To run the simulation enter "python turingn.py"

:party:
```
    func taskForPUTMethod(method: String, parameters: [String : AnyObject]?, jsonBody: [String:AnyObject], completionHandler: (result: AnyObject!, error: NSError?) -> Void) -> NSURLSessionDataTask {
        
        /* 1. Set the parameters */
        var urlString:String
        if let mutableParameters = parameters {
            urlString = method + UdacityClient.escapedParameters(mutableParameters)
        }else{
            urlString = method
        }
        
        /* 2/3. Build the URL and configure the request */
        
        let url = NSURL(string: urlString)!
        let request = NSMutableURLRequest(URL: url)
//        var jsonifyError: NSError? = nil
        request.HTTPMethod = "PUT"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.addValue(UdacityClient.Constants.ParseApplicationID, forHTTPHeaderField: "X-Parse-Application-Id")
        request.addValue(UdacityClient.Constants.ApiKey, forHTTPHeaderField: "X-Parse-REST-API-Key")
        
        do {
            request.HTTPBody = try NSJSONSerialization.dataWithJSONObject(jsonBody, options: [])
        } catch _ as NSError {
//            jsonifyError = error
            request.HTTPBody = nil
        }
        
        /* 4. Make the request */
        let task = session.dataTaskWithRequest(request) {data, response, downloadError in
            
            /* 5/6. Parse the data and use the data (happens in completion handler) */
            if let error = downloadError {
                _ = UdacityClient.errorForData(data, response: response, error: error)
                completionHandler(result: nil, error: downloadError)
            } else {
                UdacityClient.parseJSONWithCompletionHandler(data!, completionHandler: completionHandler)
            }
        }
        
        /* 7. Start the request */
        task.resume()
        
        return task
    }
 
``` 
