// APIのベースURL
const API_BASE_URL = 'http://localhost:8000/api/items';

// DOMが読み込まれたら実行
document.addEventListener('DOMContentLoaded', () => {
    // 要素の取得
    const externalIdInput = document.getElementById('externalId');
    const convertBtn = document.getElementById('convertBtn');
    const resultTableBody = document.getElementById('resultTableBody');
    const noResultsDiv = document.getElementById('noResults');
    const errorMessageDiv = document.getElementById('errorMessage');
    const resultTable = document.getElementById('resultTable');

    // 初期表示設定
    resultTable.style.display = 'none';
    noResultsDiv.style.display = 'block';

    // 変換ボタンのクリックイベント
    convertBtn.addEventListener('click', async () => {
        // 入力値の取得
        const externalId = externalIdInput.value.trim();

        // 入力チェック
        if (!externalId) {
            showError('社外品番を入力してください');
            return;
        }

        try {
            // ボタンを無効化して処理中を表示
            convertBtn.disabled = true;
            convertBtn.textContent = '検索中...';
            clearError();
            noResultsDiv.textContent = '検索中...';
            noResultsDiv.style.display = 'block';
            resultTable.style.display = 'none';
            resultTableBody.innerHTML = '';

            // APIリクエスト
            const response = await fetch(`${API_BASE_URL}?ex_id=${encodeURIComponent(externalId)}`);
            const data = await response.json();

            // レスポンスの処理
            if (response.ok) {
                if (data.data && data.data.length > 0) {
                    // 結果をテーブルに表示
                    displayResults(data.data);
                    resultTable.style.display = 'table';
                    noResultsDiv.style.display = 'none';
                } else {
                    // 結果がない場合
                    noResultsDiv.textContent = '該当する品番が見つかりませんでした';
                    noResultsDiv.style.display = 'block';
                    resultTable.style.display = 'none';
                    showError('該当する品番が見つかりませんでした');
                }
            } else {
                // APIエラーの処理
                noResultsDiv.textContent = 'エラーが発生しました';
                noResultsDiv.style.display = 'block';
                resultTable.style.display = 'none';
                showError(`APIエラー: ${data.errors ? data.errors.join(', ') : '不明なエラー'}`);
            }
        } catch (error) {
            // 通信エラーの処理
            noResultsDiv.textContent = 'エラーが発生しました';
            noResultsDiv.style.display = 'block';
            resultTable.style.display = 'none';
            showError(`通信エラー: ${error.message}`);
        } finally {
            // ボタンを元に戻す
            convertBtn.disabled = false;
            convertBtn.textContent = '変換';
        }
    });

    // Enterキーで変換ボタンをクリック
    externalIdInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            convertBtn.click();
        }
    });

    // 結果をテーブルに表示する関数
    function displayResults(items) {
        resultTableBody.innerHTML = '';

        items.forEach(item => {
            const row = document.createElement('tr');

            // ID列
            const idCell = document.createElement('td');
            idCell.textContent = item.id;
            row.appendChild(idCell);

            // 社外品番列
            const exIdCell = document.createElement('td');
            exIdCell.textContent = item.ex_id;
            row.appendChild(exIdCell);

            // 社内品番列
            const inIdCell = document.createElement('td');
            inIdCell.textContent = item.in_id;
            row.appendChild(inIdCell);

            resultTableBody.appendChild(row);
        });
    }

    // エラーメッセージの表示
    function showError(message) {
        errorMessageDiv.textContent = message;
        errorMessageDiv.style.display = 'block';
    }

    // エラーメッセージのクリア
    function clearError() {
        errorMessageDiv.textContent = '';
        errorMessageDiv.style.display = 'none';
    }
});
