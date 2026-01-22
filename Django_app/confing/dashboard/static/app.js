// Pobierz i wyświetl podsumowanie
fetch('/api/summary')
  .then(res => res.json())
  .then(data => {
    document.getElementById('revenue').textContent = data.total_revenue?.toLocaleString('pl-PL', { style: 'currency', currency: 'PLN' }) ?? '—';
    document.getElementById('cost').textContent = data.total_cost?.toLocaleString('pl-PL', { style: 'currency', currency: 'PLN' }) ?? '—';
    document.getElementById('pandl').textContent = data.total_pandl?.toLocaleString('pl-PL', { style: 'currency', currency: 'PLN' }) ?? '—';
  });

// Pobierz i wyświetl tabelę grup
fetch('/api/group')
  .then(res => res.json())
  .then(data => {
    const tbody = document.getElementById('group-table');
    tbody.innerHTML = '';
    data.forEach(row => {
      const tr = document.createElement('tr');
      const tdGroup = document.createElement('td');
      tdGroup.textContent = row.ad_group;
      const tdPnL = document.createElement('td');
      tdPnL.textContent = row.total_pandl?.toLocaleString('pl-PL', { style: 'currency', currency: 'PLN' }) ?? '—';
      tr.appendChild(tdGroup);
      tr.appendChild(tdPnL);
      tbody.appendChild(tr);
    });
  });
