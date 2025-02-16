document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-cadastro");
    const btnCancelar = document.getElementById("btn-cancelar");
  
    // Substitua pela URL da sua API Flask caso precise rodar externamente
    const BASE_URL = "http://flask-env.eba-pimaq7yt.sa-east-1.elasticbeanstalk.com";

  
    // Função para carregar os computadores, opcionalmente com um termo de busca
    function carregarComputadores(busca = '') {
      let url = `${BASE_URL}/computadores`;
      if (busca) {
        url += `?busca=${encodeURIComponent(busca)}`;
      }
      fetch(url)
        .then(response => response.json())
        .then(data => {
          const tbody = document.querySelector("#tabela-computadores tbody");
          tbody.innerHTML = ""; // Limpa a tabela
  
          if (data.length === 0) {
            tbody.innerHTML = "<tr><td colspan='9'>Nenhum computador cadastrado.</td></tr>";
          } else {
            data.forEach(comp => {
              const row = document.createElement("tr");
              row.innerHTML = `
                <td>${comp.id}</td>
                <td>${comp.nome}</td>
                <td>${comp.fabricante}</td>
                <td>${comp.modelo}</td>
                <td>${comp.serial}</td>
                <td>${comp.data_aquisicao}</td>
                <td>${comp.sistema_operacional ? comp.sistema_operacional : ""}</td>
                <td>${comp.setor ? comp.setor : ""}</td>
                <td>
                  <button class="btn-action btn-edit" data-id="${comp.id}">Editar</button>
                  <button class="btn-action btn-delete" data-id="${comp.id}">Excluir</button>
                </td>
              `;
              tbody.appendChild(row);
            });
  
            // Adiciona os event listeners para os botões de editar e excluir
            document.querySelectorAll(".btn-edit").forEach(btn => {
              btn.addEventListener("click", () => {
                const id = btn.getAttribute("data-id");
                editarFormulario(id);
              });
            });
            document.querySelectorAll(".btn-delete").forEach(btn => {
              btn.addEventListener("click", () => {
                const id = btn.getAttribute("data-id");
                if (confirm("Deseja realmente excluir este computador?")) {
                  excluirComputador(id);
                }
              });
            });
          }
        })
        .catch(err => console.error("Erro ao buscar dados:", err));
    }
  
    // Função para carregar os dados de um computador no formulário para edição
    function editarFormulario(id) {
      // Agora buscamos diretamente pelo endpoint /computadores/<id>, que retorna 1 objeto
      fetch(`${BASE_URL}/computadores/${id}`)
        .then(response => response.json())
        .then(comp => {
          if (comp.erro) {
            alert("Erro: " + comp.erro);
            return;
          }
          document.getElementById("id").value = comp.id;
          document.getElementById("nome").value = comp.nome;
          document.getElementById("fabricante").value = comp.fabricante;
          document.getElementById("modelo").value = comp.modelo;
          document.getElementById("serial").value = comp.serial;
          document.getElementById("data_aquisicao").value = comp.data_aquisicao;
          document.getElementById("sistema_operacional").value = comp.sistema_operacional || "";
          document.getElementById("setor").value = comp.setor || "";
          btnCancelar.style.display = "inline-block";
        })
        .catch(err => console.error("Erro ao carregar dados para edição:", err));
    }
  
    // Função para enviar dados para cadastrar ou editar um computador
    form.addEventListener("submit", event => {
      event.preventDefault();
  
      const id = document.getElementById("id").value;
      const novoComp = {
        nome: document.getElementById("nome").value,
        fabricante: document.getElementById("fabricante").value,
        modelo: document.getElementById("modelo").value,
        serial: document.getElementById("serial").value,
        data_aquisicao: document.getElementById("data_aquisicao").value,
        sistema_operacional: document.getElementById("sistema_operacional").value,
        setor: document.getElementById("setor").value,
      };
  
      if (id) {
        // Se houver um id, atualiza (PUT)
        fetch(`${BASE_URL}/computadores/${id}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(novoComp)
        })
        .then(response => response.json())
        .then(data => {
          console.log("Computador atualizado:", data);
          form.reset();
          document.getElementById("id").value = "";
          btnCancelar.style.display = "none";
          carregarComputadores();
        })
        .catch(err => console.error("Erro ao atualizar:", err));
      } else {
        // Caso contrário, cria (POST)
        fetch(`${BASE_URL}/computadores`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(novoComp)
        })
        .then(response => response.json())
        .then(data => {
          console.log("Computador cadastrado:", data);
          form.reset();
          carregarComputadores();
        })
        .catch(err => console.error("Erro ao cadastrar:", err));
      }
    });
  
    // Botão para cancelar a edição e limpar o formulário
    btnCancelar.addEventListener("click", () => {
      form.reset();
      document.getElementById("id").value = "";
      btnCancelar.style.display = "none";
    });
  
    // Função para excluir um computador
    function excluirComputador(id) {
      fetch(`${BASE_URL}/computadores/${id}`, {
        method: "DELETE"
      })
      .then(response => response.json())
      .then(data => {
        console.log("Computador excluído:", data);
        carregarComputadores();
      })
      .catch(err => console.error("Erro ao excluir:", err));
    }
  
    // Evento para a busca
    const btnBusca = document.getElementById("btn-busca");
    btnBusca.addEventListener("click", () => {
      const termoBusca = document.getElementById("campo-busca").value;
      carregarComputadores(termoBusca);
    });
  
    // Carrega os computadores ao iniciar a página
    carregarComputadores();
  });
  