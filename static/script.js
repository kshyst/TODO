        function addTask() {
            let taskInput = document.getElementById("taskInput");
            let dueDateInput = document.getElementById("dueDateInput");
            let taskText = taskInput.value.trim();
            let dueDate = dueDateInput.value;
            if (taskText === "") return;

            let li = document.createElement("li");
            li.innerHTML = `<input type='checkbox' class='check' onclick='toggleTask(this)'> ${taskText} (Due: ${dueDate})`;
            document.getElementById("taskList").appendChild(li);
            taskInput.value = "";
            dueDateInput.value = "";
        }

        function toggleTask(checkbox) {
            checkbox.parentElement.classList.toggle("completed");
        }