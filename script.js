let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

function save() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
  show();
}

function addTask() {
  let input = document.getElementById("taskInput");
  let text = input.value.trim();
  if (text === "") return;
  tasks.push({ text: text, done: false });
  input.value = "";
  save();
}

function show() {
  let list = document.getElementById("taskList");
  list.innerHTML = "";
  tasks.forEach((t, i) => {
    list.innerHTML += `
      <li class="${t.done ? 'done' : ''}">
        <span onclick="toggleTask(${i})" style="cursor:pointer">
          ${t.done ? '✅' : '⬜'} ${t.text}
        </span>
        <button class="del" onclick="deleteTask(${i})">X</button>
      </li>`;
  });
  let doneCount = tasks.filter(t => t.done).length;
  document.getElementById("count").innerText =
    `Done: ${doneCount} / Total: ${tasks.length}`;
}

function toggleTask(i) {
  tasks[i].done = !tasks[i].done;
  save();
}

function deleteTask(i) {
  tasks.splice(i, 1);
  save();
}

function clearAll() {
  tasks = [];
  save();
}

// Enter key also adds
document.getElementById("taskInput").addEventListener("keypress", function(e) {
  if (e.key === "Enter") addTask();
});

show();