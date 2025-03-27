param (
    [Parameter(Mandatory=$true)]
    [string]$method,

    [Parameter(Mandatory=$false)]
    [string]$item_id,

    [Parameter(Mandatory=$false)]
    [string]$ex_id,

    [Parameter(Mandatory=$false)]
    [string]$in_id,

    [Parameter(Mandatory=$false)]
    [string]$json_data
)

# APIのベースURL
$base_url = "http://localhost:8000/api/items"

# 結果を格納するオブジェクト
$result = @{
    success = $false
    data = $null
    error = $null
}

try {
    # リクエストヘッダー
    $headers = @{
        "Content-Type" = "application/json"
        "Accept" = "application/json"
    }

    # メソッドに応じた処理
    switch ($method) {
        "GET" {
            # URLの構築
            $url = $base_url

            # 特定のIDが指定されている場合
            if ($item_id) {
                $url = "$base_url/$item_id"
            }
            # 検索条件がある場合はクエリパラメータを追加
            else {
                $query_params = @()
                if ($ex_id) { $query_params += "ex_id=$ex_id" }
                if ($in_id) { $query_params += "in_id=$in_id" }

                if ($query_params.Count -gt 0) {
                    $url += "?" + ($query_params -join "&")
                }
            }

            $response = Invoke-RestMethod -Uri $url -Method Get -Headers $headers
        }
        "POST" {
            # 新規作成
            $response = Invoke-RestMethod -Uri $base_url -Method Post -Headers $headers -Body $json_data
        }
        "PUT" {
            # 更新
            if (-not $item_id) {
                throw "PUT操作にはitem_idが必要です"
            }
            $url = "$base_url/$item_id"
            $response = Invoke-RestMethod -Uri $url -Method Put -Headers $headers -Body $json_data
        }
        "DELETE" {
            # 削除
            if (-not $item_id) {
                throw "DELETE操作にはitem_idが必要です"
            }
            $url = "$base_url/$item_id"
            $response = Invoke-RestMethod -Uri $url -Method Delete -Headers $headers
        }
        default {
            throw "サポートされていないメソッドです: $method"
        }
    }

    # 成功した場合
    $result.success = $true
    $result.data = $response
}
catch {
    # エラーの場合
    $result.error = $_.Exception.Message
}

# 結果をJSON形式で返す
return $result | ConvertTo-Json -Depth 10
