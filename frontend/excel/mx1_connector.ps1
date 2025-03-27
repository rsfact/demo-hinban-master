param (
    [string]$method,
    [string]$item_id = "",
    [string]$ex_id = "",
    [string]$in_id = "",
    [string]$json_data = ""
)

# Base URL for API
$baseUrl = "http://localhost:8000/api/items"

# Prepare HTTP headers
$headers = @{
    "Content-Type" = "application/json"
    "Accept" = "application/json"
}

# Process based on method
$methodUpper = $method.ToUpper()

# GET method
if ($methodUpper -eq "GET") {
    # Get by ID
    if ($item_id -ne "") {
        $url = "$baseUrl/$item_id"
        $result = Invoke-RestMethod -Uri $url -Method Get -Headers $headers
    }
    # Search by criteria
    elseif ($ex_id -ne "" -or $in_id -ne "") {
        $queryParams = @()
        if ($ex_id -ne "") { $queryParams += "ex_id=$ex_id" }
        if ($in_id -ne "") { $queryParams += "in_id=$in_id" }

        $queryString = [string]::Join("&", $queryParams)
        $url = "$baseUrl/?$queryString"

        $result = Invoke-RestMethod -Uri $url -Method Get -Headers $headers
    }
    # Get all
    else {
        $result = Invoke-RestMethod -Uri $baseUrl -Method Get -Headers $headers
    }

    # Convert response to JSON and output
    $result | ConvertTo-Json -Depth 10
}
# POST method
elseif ($methodUpper -eq "POST") {
    # JSON data is required
    if ($json_data -eq "") {
        Write-Error "POST request requires JSON data"
        exit 1
    }

    $result = Invoke-RestMethod -Uri $baseUrl -Method Post -Headers $headers -Body $json_data

    # Convert response to JSON and output
    $result | ConvertTo-Json -Depth 10
}
# PUT method
elseif ($methodUpper -eq "PUT") {
    # Item ID is required
    if ($item_id -eq "") {
        Write-Error "PUT request requires item_id"
        exit 1
    }

    # Use empty JSON if not provided
    if ($json_data -eq "") {
        $json_data = "{}"
    }

    $url = "$baseUrl/$item_id"
    $result = Invoke-RestMethod -Uri $url -Method Put -Headers $headers -Body $json_data

    # Convert response to JSON and output
    $result | ConvertTo-Json -Depth 10
}
# DELETE method
elseif ($methodUpper -eq "DELETE") {
    # Item ID is required
    if ($item_id -eq "") {
        Write-Error "DELETE request requires item_id"
        exit 1
    }

    $url = "$baseUrl/$item_id"
    $result = Invoke-RestMethod -Uri $url -Method Delete -Headers $headers

    # Convert response to JSON and output
    $result | ConvertTo-Json -Depth 10
}
# Unsupported method
else {
    Write-Error "Unsupported HTTP method: $method"
    exit 1
}
