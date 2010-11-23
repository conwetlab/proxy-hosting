var Proxy = {};

/**
 * HTTP proxy invocation
 *
 * Parameters:
 *   url     target url
 *   params  see http://api.prototypejs.org/ajax/ajax/request/
 */
Proxy.send = function(url, params) {
    new Ajax.Request(Proxy.buildProxyURL(url), params);
}


Proxy.buildProxyURL = function(url) {
        var final_url = url;

        var protocolEnd = url.indexOf('://');
        if (protocolEnd != -1) {
                var domainStart = protocolEnd + 3;
                var pathStart = url.indexOf('/', domainStart);
                if (pathStart == -1) {
                    pathStart = url.length;
                }

                var protocol = url.substr(0, protocolEnd);
                var domain = url.substr(domainStart, pathStart - domainStart);
                var rest = url.substring(pathStart);

                final_url = "/proxy" + '/' +
                            encodeURIComponent(protocol) + '/' +
                            encodeURIComponent(domain) + rest;
        }   

        return final_url;

}
