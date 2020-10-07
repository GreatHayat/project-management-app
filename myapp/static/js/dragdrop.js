
let list_group_item = "";
document.querySelectorAll(".list-group-item").forEach(function (list_item) {
    list_item.addEventListener("dragstart", function () {
        list_item.classList.add("bg-primary");
        list_group_item = list_item;
        //console.log(list_group_item);
    });
});
document.querySelectorAll(".list-group-item").forEach(function (list_item) {
    list_item.addEventListener("dragend", function () {
        list_item.classList.add("bg-primary");
    });
});
document.querySelectorAll(".card-body").forEach(function (list_group) {
    list_group.addEventListener("dragover", function (e) {
        e.preventDefault();
    });
});

document.querySelectorAll(".card-body").forEach(function (list_group) {
    list_group.addEventListener("dragenter", function () {
        list_group.classList.add("bg-secondary");
    });
});

document.querySelectorAll(".card-body").forEach(function (list_group) {
    list_group.addEventListener("dragleave", function () {
        list_group.classList.remove("bg-secondary");
    });
});
document.querySelectorAll(".card-body").forEach(function (list_group) {
    list_group.addEventListener("drop", function () {
        const URL = `http://127.0.0.1:8000/update-task-${list_group.dataset.type}/${list_group_item.dataset.id}`;
        console.log("tAB URL", `http://127.0.0.1:8000/update-task-${list_group.dataset.type}/${list_group_item.dataset.id}`)
        fetch(URL)
            .then(res => res.json())
            .then(result => {
                list_group_item.classList.remove("bg-primary");
                list_group_item.classList.add("bg-warning", "text-white");
                list_group.children[0].append(list_group_item);
                list_group.classList.remove("bg-secondary");
                Toastify({
                    text: result.message,
                    backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
                    position: 'top-left',
                    close: true,
                    className: "info",
                }).showToast();
            })
            .catch(error => console.log(error))
    });
});