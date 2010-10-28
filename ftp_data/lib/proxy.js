var Proxy = {};

/**
 * HTTP proxy invocation
 *
 * Parameters:
 *   url     target url
 *   params  see http://api.prototypejs.org/ajax/ajax/request/
 */
Proxy.send = function(url, params) {
    var method = params.method || "post";
    delete params.method;
    
    var requestParameters = params.parameters;
    delete params.parameters; 
    
    params.parameters = {
        "url": url,
        "method": method,
        "params": requestParameters
    };
    params.method = "POST";
    
    new Ajax.Request("/proxy", params);
}
