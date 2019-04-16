let list = [];
let filteredList = [];

const filterList = function(query) {
    filteredList = list.filter(item => item.toLowerCase().includes(query.toLowerCase()));
    list.forEach(item => {
        document.getElementById(item).hidden = !filteredList.includes(item);
    })
};

const setItemList = function(items) {
    const filterI = document.getElementById('filter-input');
    filterI.addEventListener('input', e => filterList(e.target.value));
    list = items;
};

export {filterList, setItemList};

