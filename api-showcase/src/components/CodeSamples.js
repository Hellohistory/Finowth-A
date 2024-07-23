export const generateCodeSample = (api, language, postParams = {}) => {
  switch (language) {
    case 'Python':
      return generatePythonSample(api, postParams);
    case 'Rust':
      return generateRustSample(api, postParams);
    case 'C++':
      return generateCppSample(api, postParams);
    case 'Java':
      return generateJavaSample(api, postParams);
    case 'JavaScript':
      return generateJavaScriptSample(api, postParams);
    case 'Go':
      return generateGoSample(api, postParams);
    case 'PHP':
      return generatePHPSample(api, postParams);
    case 'R':
      return generateRSample(api, postParams);
    case 'Ruby':
      return generateRubySample(api, postParams);
    case 'C#':
      return generateCSharpSample(api, postParams);
    case 'Lua':
      return generateLuaSample(api, postParams);
    case 'VB':
      return generateVBSample(api, postParams);
    case 'Kotlin':
      return generateKotlinSample(api, postParams);
    case 'MATLAB':
      return generateMATLABSample(api, postParams);
    case 'Swift':
      return generateSwiftSample(api, postParams);
    case 'Objective-C':
      return generateObjectiveCSample(api, postParams);
    case 'Dart':
      return generateDartSample(api, postParams);
    case 'Perl':
      return generatePerlSample(api, postParams);
    case 'Haskell':
      return generateHaskellSample(api, postParams);
    case 'Elixir':
      return generateElixirSample(api, postParams);
    case 'Shell':
      return generateShellSample(api, postParams);
    case 'TypeScript':
      return generateTypeScriptSample(api, postParams);
    case 'Groovy':
      return generateGroovySample(api, postParams);
    case 'F#':
      return generateFSharpSample(api, postParams);
    default:
      return '';
  }
};


const generatePythonSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import requests
import json

url = 'http://localhost:36925${api.api_path}'

response = requests.get(url)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    '${key}': ${JSON.stringify(value)}`)
      .join(',\n');
    return `import requests
import json

url = 'http://localhost:36925${api.api_path}'
data = {
${params}
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)`;
  }
};


const generateRustSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `use reqwest;
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let url = "http://localhost:36925${api.api_path}";
    let response = reqwest::get(url).await?;

    match response.status() {
        reqwest::StatusCode::OK => {
            let body = response.text().await?;
            println!("{}", body);
        },
        _ => println!("Error: {}", response.status()),
    }

    Ok(())
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        "${key}": ${JSON.stringify(value)}`)
      .join(',\n');
    return `use reqwest::{Client, Response};
use serde_json::json;
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let url = "http://localhost:36925${api.api_path}";
    let client = Client::new();
    let data = json!({
${params}
    });

    let response: Response = client.post(url)
        .json(&data)
        .send()
        .await?;

    match response.status() {
        reqwest::StatusCode::OK => {
            let body = response.text().await?;
            println!("{}", body);
        },
        _ => println!("Error: {}", response.status()),
    }

    Ok(())
}`;
}
};

const generateCppSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `#include <iostream>
#include <cpr/cpr.h>

int main() {
    std::string url = "http://localhost:36925${api.api_path}";
    cpr::Response response = cpr::Get(cpr::Url{url});
    if (response.status_code == 200) {
        std::cout << response.text << std::endl;
    } else {
        std::cout << "HTTP error code: " << response.status_code << std::endl;
    }
    return 0;
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        {"${key}", "${value}"}`)
      .join(",\n");
    return `#include <iostream>
#include <cpr/cpr.h>

int main() {
    std::string url = "http://localhost:36925${api.api_path}";
    cpr::Payload{${params}};
    cpr::Response response = cpr::Post(cpr::Url{url}, payload);
    if (response.status_code == 200) {
        std::cout << response.text << std::endl;
    } else {
        std::cout << "HTTP error code: " << response.status_code << std::endl;
    }
    return 0;
}`;
  }
};

const generateJavaSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        String urlString = "http://localhost:36925${api.api_path}";
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        int responseCode = conn.getResponseCode();
        if (responseCode == 200) {
            Scanner scanner = new Scanner(url.openStream());
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }
            scanner.close();
        } else {
            System.out.println("HTTP error code: " + responseCode);
        }
    }
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        put("${key}", ${JSON.stringify(value)});`)
      .join('\n');
    return `import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import org.json.JSONObject;

public class Main {
    public static void main(String[] args) throws IOException {
        String urlString = "http://localhost:36925${api.api_path}";
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json; utf-8");
        conn.setDoOutput(true);
        JSONObject json = new JSONObject() {{
${params}
        }};
        try(OutputStream os = conn.getOutputStream()) {
            byte[] input = json.toString().getBytes(StandardCharsets.UTF_8);
            os.write(input, 0, input.length);
        }
        int responseCode = conn.getResponseCode();
        if (responseCode == 200) {
            Scanner scanner = new Scanner(conn.getInputStream());
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }
            scanner.close();
        } else {
            System.out.println("HTTP error code: " + responseCode);
        }
    }
}`;
  }
};

const generateJavaScriptSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `fetch('http://localhost:36925${api.api_path}')
    .then(response => {
        if (!response.ok) {
            throw new Error(\`HTTP error! status: \${response.status}\`);
        }
        return response.json();
    })
    .then(data => console.log(JSON.stringify(data, null, 4)))
    .catch(error => console.error('Error:', error));`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = JSON.stringify(postParams, null, 4)
      .split('\n')
      .map(line => `    ${line}`)
      .join('\n');
    return `fetch('http://localhost:36925${api.api_path}', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
${params}
    })
})
    .then(response => {
        if (!response.ok) {
            throw new Error(\`HTTP error! status: \${response.status}\`);
        }
        return response.json();
    })
    .then(data => console.log(JSON.stringify(data, null, 4)))
    .catch(error => console.error('Error:', error));`;
  }
};


const generateGoSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    url := "http://localhost:36925${api.api_path}"
    response, err := http.Get(url)
    if err != nil {
        fmt.Println(err)
        return
    }
    defer response.Body.Close()
    if response.StatusCode == http.StatusOK {
        body, _ := ioutil.ReadAll(response.Body)
        fmt.Println(string(body))
    } else {
        fmt.Println(response.StatusCode)
    }
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}": ${JSON.stringify(value)}`)
      .join(",\n");
    return `package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "io/ioutil"
)

func main() {
    url := "http://localhost:36925${api.api_path}"
    data := map[string]interface{}{
${params}
    }
    jsonData, _ := json.Marshal(data)
    response, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        fmt.Println(err)
        return
    }
    defer response.Body.Close()
    if response.StatusCode == http.StatusOK {
        body, _ := ioutil.ReadAll(response.Body)
        fmt.Println(string(body))
    } else {
        fmt.Println(response.StatusCode)
    }
}`;
  }
};

const generateDartSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  var url = Uri.parse('http://localhost:36925${api.api_path}');
  var response = await http.get(url);
  if (response.statusCode == 200) {
    print(json.decode(response.body));
  } else {
    print(response.statusCode);
  }
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `      '${key}': '${value}'`)
      .join(",\n");
    return `import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  var url = Uri.parse('http://localhost:36925${api.api_path}');
  var data = {
${params}
  };
  var response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: json.encode(data),
  );
  if (response.statusCode == 200) {
    print(json.decode(response.body));
  } else {
    print(response.statusCode);
  }
}`;
  }
};


const generatePHPSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `<?php

$url = 'http://localhost:36925${api.api_path}';
$options = [
    'http' => [
        'method' => 'GET',
        'header' => 'Content-Type: application/json'
    ]
];
$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);

if ($response === FALSE) {
    echo "Error: Unable to fetch the URL.\n";
} else {
    $http_code = $http_response_header[0];
    if (strpos($http_code, '200') !== false) {
        echo $response;
    } else {
        echo "HTTP Error: " . $http_code . "\n";
    }
}

?>`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}" => "${value}"`)
      .join(",\n");
    return `<?php

$url = 'http://localhost:36925${api.api_path}';
$data = json_encode([
${params}
]);

$options = [
    'http' => [
        'header'  => "Content-Type: application/json\\r\\n",
        'method'  => 'POST',
        'content' => $data,
    ],
];
$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);

if ($response === FALSE) {
    echo "Error: Unable to post to the URL.\n";
} else {
    $http_code = $http_response_header[0];
    if (strpos($http_code, '200') !== false) {
        echo $response;
    } else {
        echo "HTTP Error: " . $http_code . "\n";
    }
}

?>`;
  }
};


const generateRSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `url <- "http://localhost:36925${api.api_path}"
response <- httr::GET(url)
if (httr::status_code(response) == 200) {
    cat(httr::content(response, "text"))
} else {
    cat(httr::status_code(response))
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `  "${key}" = ${JSON.stringify(value)}`)
      .join(",\n");
    return `url <- "http://localhost:36925${api.api_path}"
data <- list(
${params}
)
response <- httr::POST(url, body = jsonlite::toJSON(data, auto_unbox = TRUE), encode = "json")
if (httr::status_code(response) == 200) {
    cat(httr::content(response, "text"))
} else {
    cat(httr::status_code(response))
}`;
  }
};

const generateRubySample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `require 'net/http'
require 'json'

url = URI('http://localhost:36925${api.api_path}')
response = Net::HTTP.get_response(url)
if response.code.to_i == 200
  puts JSON.pretty_generate(JSON.parse(response.body))
else
  puts response.code
end`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `  "${key}" => ${JSON.stringify(value)}`)
      .join(",\n");
    return `require 'net/http'
require 'json'

url = URI('http://localhost:36925${api.api_path}')
http = Net::HTTP.new(url.host, url.port)
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request.body = {\n${params}\n}.to_json
response = http.request(request)
if response.code.to_i == 200
  puts JSON.pretty_generate(JSON.parse(response.body))
else
  puts response.code
end`;
  }
};

const generateCSharpSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        HttpClient client = new HttpClient();
        HttpResponseMessage response = await client.GetAsync("http://localhost:36925${api.api_path}");
        if (response.IsSuccessStatusCode) {
            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine(responseBody);
        } else {
            Console.WriteLine($"Error: {(int)response.StatusCode} - {response.ReasonPhrase}");
        }
    }
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `            "${key}" = ${JSON.stringify(value)}`)
      .join(",\n");
    return `using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        HttpClient client = new HttpClient();
        var data = new {
${params}
        };
        StringContent content = new StringContent(JsonSerializer.Serialize(data), Encoding.UTF8, "application/json");
        HttpResponseMessage response = await client.PostAsync("http://localhost:36925${api.api_path}", content);
        if (response.IsSuccessStatusCode) {
            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine(responseBody);
        } else {
            Console.WriteLine($"Error: {(int)response.StatusCode} - {response.ReasonPhrase}");
        }
    }
}`;
  }
};

const generateLuaSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `local http = require("socket.http")
local ltn12 = require("ltn12")

local url = "http://localhost:36925${api.api_path}"
local response_body = {}
local res, code, response_headers, status = http.request{
    url = url,
    sink = ltn12.sink.table(response_body)
}
if code == 200 then
    print(table.concat(response_body))
else
    print(code)
end`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        ["${key}"] = "${value}"`)
      .join(",\n");
    return `local http = require("socket.http")
local ltn12 = require("ltn12")
local json = require("cjson")

local url = "http://localhost:36925${api.api_path}"
local request_body = json.encode({
${params}
})
local response_body = {}
local res, code, response_headers, status = http.request{
    url = url,
    method = "POST",
    headers = {
        ["Content-Type"] = "application/json",
        ["Content-Length"] = tostring(#request_body)
    },
    source = ltn12.source.string(request_body),
    sink = ltn12.sink.table(response_body)
}
if code == 200 then
    print(table.concat(response_body))
else
    print(code)
end`;
  }
};

const generateVBSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `Dim http As Object
Set http = CreateObject("MSXML2.XMLHTTP")
http.Open "GET", "http://localhost:36925${api.api_path}", False
http.send
If http.Status = 200 Then
    WScript.Echo http.responseText
Else
    WScript.Echo http.Status
End If`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    """" & "${key}" & """: """" & "${value}" & """",`)
      .join("\n");
    return `Dim http As Object
Set http = CreateObject("MSXML2.XMLHTTP")
Dim data As String
http.Open "POST", "http://localhost:36925${api.api_path}", False
http.setRequestHeader "Content-Type", "application/json"
data = "{${params}
}"
http.send data
If http.Status = 200 Then
    WScript.Echo http.responseText
Else
    WScript.Echo http.Status
End If`;
  }
};

const generateKotlinSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import java.net.HttpURLConnection
import java.net.URL

fun main() {
    val url = URL("http://localhost:36925${api.api_path}")
    with(url.openConnection() as HttpURLConnection) {
        requestMethod = "GET"
        println("Response Code: $responseCode")
        if (responseCode == 200) {
            inputStream.bufferedReader().use {
                it.lines().forEach { line ->
                    println(line)
                }
            }
        } else {
            println(responseCode)
        }
    }
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        "${key}" to ${JSON.stringify(value)}`)
      .join(",\n");
    return `import java.net.HttpURLConnection
import java.net.URL
import java.io.OutputStreamWriter
import java.io.BufferedWriter
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper

fun main() {
    val url = URL("http://localhost:36925${api.api_path}")
    with(url.openConnection() as HttpURLConnection) {
        requestMethod = "POST"
        setRequestProperty("Content-Type", "application/json; utf-8")
        doOutput = true

        val jsonInputString = jacksonObjectMapper().writeValueAsString(mapOf(
${params}
        ))

        outputStream.bufferedWriter().use { it.write(jsonInputString) }

        println("Response Code: $responseCode")
        if (responseCode == 200) {
            inputStream.bufferedReader().use {
                it.lines().forEach { line ->
                    println(line)
                }
            }
        } else {
            println(responseCode)
        }
    }
}`;
  }
};

const generateMATLABSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `url = 'http://localhost:36925${api.api_path}';
options = weboptions('RequestMethod', 'get');
response = webread(url, options);
disp(response);`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}", "${value}"`)
      .join(",\n");
    return `url = 'http://localhost:36925${api.api_path}';
data = struct(${params});
options = weboptions('RequestMethod', 'post', 'MediaType', 'application/json');
response = webwrite(url, data, options);
disp(response);`;
  }
};

const generateSwiftSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import Foundation

let url = URL(string: "http://localhost:36925${api.api_path}")!

let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print("Error: \\(error)")
        return
    }
    guard let httpResponse = response as? HTTPURLResponse else {
        print("Invalid response")
        return
    }
    guard httpResponse.statusCode == 200 else {
        print("HTTP Status Code: \\(httpResponse.statusCode)")
        return
    }
    if let data = data {
        print("Response data: \\(String(data: data, encoding: .utf8) ?? "")")
    }
}
task.resume()

RunLoop.main.run() // To keep the command line tool running
`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        "${key}": "${value}"`)
      .join(",\n");
    return `import Foundation

let url = URL(string: "http://localhost:36925${api.api_path}")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")

let json: [String: Any] = [
${params}
]
let jsonData = try! JSONSerialization.data(withJSONObject: json)

let task = URLSession.shared.uploadTask(with: request, from: jsonData) { data, response, error in
    if let error = error {
        print("Error: \\(error)")
        return
    }
    guard let httpResponse = response as? HTTPURLResponse else {
        print("Invalid response")
        return
    }
    guard httpResponse.statusCode == 200 else {
        print("HTTP Status Code: \\(httpResponse.statusCode)")
        return
    }
    if let data = data {
        print("Response data: \\(String(data: data, encoding: .utf8) ?? "")")
    }
}
task.resume()

RunLoop.main.run() // To keep the command line tool running
`;
  }
};

const generateObjectiveCSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSURL *url = [NSURL URLWithString:@"http://localhost:36925${api.api_path}"];
        NSURLRequest *request = [NSURLRequest requestWithURL:url];
        NSURLSession *session = [NSURLSession sharedSession];
        NSURLSessionDataTask *task = [session dataTaskWithRequest:request
            completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
            if (error) {
                NSLog(@"%@", error);
                return;
            }
            NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
            if (httpResponse.statusCode == 200) {
                NSString *responseString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
                NSLog(@"%@", responseString);
            } else {
                NSLog(@"%ld", (long)httpResponse.statusCode);
            }
        }];
        [task resume];
        [[NSRunLoop currentRunLoop] run]; // To keep the command-line tool running until the task is finished
    }
    return 0;
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `        @"${key}": @"${value}"`)
      .join(",\n");
    return `#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSURL *url = [NSURL URLWithString:@"http://localhost:36925${api.api_path}"];
        NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
        request.HTTPMethod = @"POST";
        [request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
        NSDictionary *json = @{
${params}
        };
        NSData *jsonData = [NSJSONSerialization dataWithJSONObject:json options:0 error:nil];
        request.HTTPBody = jsonData;
        NSURLSession *session = [NSURLSession sharedSession];
        NSURLSessionDataTask *task = [session dataTaskWithRequest:request
            completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
            if (error) {
                NSLog(@"%@", error);
                return;
            }
            NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
            if (httpResponse.statusCode == 200) {
                NSString *responseString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
                NSLog(@"%@", responseString);
            } else {
                NSLog(@"%ld", (long)httpResponse.statusCode);
            }
        }];
        [task resume];
        [[NSRunLoop currentRunLoop] run]; // To keep the command-line tool running until the task is finished
    }
    return 0;
}`;
  }
};

const generatePerlSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `use LWP::Simple;
use JSON;

my $url = 'http://localhost:36925${api.api_path}';
my $response = get($url);
if ($response) {
    print encode_json($response);
} else {
    print "Error: $response";
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}" => "${value}"`)
      .join(",\n");
    return `use LWP::UserAgent;
use HTTP::Request::Common qw(POST);
use JSON;

my $url = 'http://localhost:36925${api.api_path}';
my $ua = LWP::UserAgent->new;
my $response = $ua->request(POST $url, Content => encode_json({\n${params}\n}));

if ($response->is_success) {
    print $response->decoded_content;
} else {
    print $response->status_line;
}`;
  }
};



const generateHaskellSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import Network.HTTP.Simple
import Data.ByteString.Lazy.Char8 as L8

main :: IO ()
main = do
  let request = "GET http://localhost:36925${api.api_path}"
  response <- httpLBS request
  let statusCode = getResponseStatusCode response
  if statusCode == 200
    then L8.putStrLn $ getResponseBody response
    else print statusCode
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `("${key}", "${value}")`)
      .join(", ");
    return `import Network.HTTP.Simple
import Data.Aeson (object, (.=), encode)
import qualified Data.ByteString.Lazy.Char8 as L8

main :: IO ()
main = do
  let request = setRequestMethod "POST"
              $ setRequestPath "${api.api_path}"
              $ setRequestHost "localhost"
              $ setRequestPort 36925
              $ setRequestHeader "Content-Type" ["application/json"]
              $ setRequestBodyJSON (object [${params}])
              $ defaultRequest
  response <- httpLBS request
  let statusCode = getResponseStatusCode response
  if statusCode == 200
    then L8.putStrLn $ getResponseBody response
    else print statusCode
}`;
  }
};

const generateElixirSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `{:ok, response} = HTTPoison.get("http://localhost:36925${api.api_path}")
case response.status_code do
  200 -> IO.puts response.body
  _ -> IO.puts "Error: #{response.status_code}"
end`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}" => "${value}"`)
      .join(",\n");
    return `headers = [{"Content-Type", "application/json"}]
body = Jason.encode!(%{\n${params}\n})
{:ok, response} = HTTPoison.post("http://localhost:36925${api.api_path}", body, headers)
case response.status_code do
  200 -> IO.puts response.body
  _ -> IO.puts "Error: #{response.status_code}"
end`;
  }
};

const generateShellSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `#!/bin/bash
response=$(curl -s -w "%{http_code}" -o response.txt http://localhost:36925${api.api_path})
if [ "$response" -eq 200 ]; then
  cat response.txt
else
  echo "Error: $response"
fi`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = JSON.stringify(postParams);
    return `#!/bin/bash
response=$(curl -s -w "%{http_code}" -o response.txt -X POST http://localhost:36925${api.api_path} -H "Content-Type: application/json" -d '${params}')
if [ "$response" -eq 200 ]; then
  cat response.txt
else
  echo "Error: $response"
fi`;
  }
};

const generateTypeScriptSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `import fetch from 'node-fetch';

(async () => {
  const response = await fetch('http://localhost:36925${api.api_path}');
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    console.log(response.status);
  }
})();`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = JSON.stringify(postParams, null, 2);
    return `import fetch from 'node-fetch';

(async () => {
  const response = await fetch('http://localhost:36925${api.api_path}', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(${params}),
  });
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    console.log(response.status);
  }
})();`;
  }
};

const generateGroovySample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `@Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')
import groovyx.net.http.RESTClient

def client = new RESTClient('http://localhost:36925${api.api_path}')
def response = client.get([:])
if (response.status == 200) {
  println response.data
} else {
  println response.status
}`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}": "${value}"`)
      .join(",\n");
    return `@Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')
import groovyx.net.http.RESTClient

def client = new RESTClient('http://localhost:36925${api.api_path}')
def response = client.post(
  path: '${api.api_path}',
  body: [${params}],
  requestContentType: 'application/json'
)
if (response.status == 200) {
  println response.data
} else {
  println response.status
}`;
  }
};

const generateFSharpSample = (api, postParams) => {
  if (api.method.toUpperCase() === 'GET') {
    return `open System
open System.Net.Http
open System.Threading.Tasks

[<EntryPoint>]
let main argv =
    let url = "http://localhost:36925${api.api_path}"
    let client = new HttpClient()
    let response = client.GetAsync(url).Result
    if response.IsSuccessStatusCode then
        printfn "%s" (response.Content.ReadAsStringAsync().Result)
    else
        printfn "%d" (int response.StatusCode)
     0`;
  } else if (api.method.toUpperCase() === 'POST') {
    const params = Object.entries(postParams)
      .map(([key, value]) => `    "${key}", "${value}"`)
      .join(",\n");
    return `open System
open System.Net.Http
open System.Text
open System.Threading.Tasks
open Newtonsoft.Json

[<EntryPoint>]
let main argv =
    let url = "http://localhost:36925${api.api_path}"
    let client = new HttpClient()
    let data = [|${params}|] |> dict |> JsonConvert.SerializeObject
    let content = new StringContent(data, Encoding.UTF8, "application/json")
    let response = client.PostAsync(url, content).Result
    if response.IsSuccessStatusCode then
        printfn "%s" (response.Content.ReadAsStringAsync().Result)
    else
        printfn "%d" (int response.StatusCode)
    0`;
  }
};

