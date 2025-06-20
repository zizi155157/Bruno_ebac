{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KJqp9AANOCtf"
      },
      "source": [
        "<img src=\"https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png\" alt=\"ebac-logo\">\n",
        "\n",
        "---\n",
        "\n",
        "# **Módulo** | Análise de Dados: Controle de Versão III\n",
        "Caderno de **Exercícios**<br>\n",
        "Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d9jDtUbDOE1-"
      },
      "source": [
        "# **Tópicos**\n",
        "\n",
        "<ol type=\"1\">\n",
        "  <li>Sistema de branchs;</li>\n",
        "  <li>Trabalhando com branchs;</li>\n",
        "  <li>Mover código entre branchs.</li>\n",
        "</ol>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SmoHgt-lwkpD"
      },
      "source": [
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GABI6OW8OfQ2"
      },
      "source": [
        "# **Exercícios**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kzRDceCvkFj2"
      },
      "source": [
        "## 1\\. Setup"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WCQi-s0Hpd5V"
      },
      "source": [
        "Para realizar os exercicios vamos configurar o `git` e trazer o projeto do GitHub para a a máquina virtual do Google Colab (ou na sua máquina local, as instruções são as mesmas). Para tanto, replique as atividades expostas na aula 1 deste módulo."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HrTLgE0tki6P"
      },
      "source": [
        "### **1.1. Autenticação**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7tIjNOs8q6aZ"
      },
      "source": [
        "Nesta etapa, vamos configura o `git` com suas credenciais."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IwTTh4VKkdKN"
      },
      "source": [
        "import os\n",
        "\n",
        "username = \"<seu-usuario-git>\" # insira o seu nome de usuário do git\n",
        "os.environ[\"GITHUB_USER\"] = username\n",
        "\n",
        "!git config --global user.name \"${GITHUB_USER}\""
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8gt4Y28skdKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "945bccd9-e870-4f81-e53b-4805de4eb530"
      },
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "usermail = getpass()\n",
        "os.environ[\"GITHUB_MAIL\"] = usermail\n",
        "\n",
        "!git config --global user.email \"${GITHUB_MAIL}\""
      ],
      "execution_count": 2,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BS6vMNnCkdKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "29afeaae-cad8-4afa-8cc6-93318bfcca42"
      },
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "usertoken = getpass()\n",
        "os.environ[\"GITHUB_TOKEN\"] = usertoken"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TTh7w8rgkznY"
      },
      "source": [
        "### **1.2. Projeto**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "clBerimQs2PY"
      },
      "source": [
        "Nesta etapa, vamos trazer o projeto do GitHub para máquina local."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fohdVuLzkdKP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c001d417-2397-45ec-a7f8-fdb5755d0f60"
      },
      "source": [
        "!git clone https://github.com/EDVADMBD/turbo-invention.git # insira o link do seu repositório remoto"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'turbo-invention'...\n",
            "remote: Enumerating objects: 13, done.\u001b[K\n",
            "remote: Counting objects: 100% (13/13), done.\u001b[K\n",
            "remote: Compressing objects: 100% (10/10), done.\u001b[K\n",
            "remote: Total 13 (delta 2), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (13/13), 486.64 KiB | 7.49 MiB/s, done.\n",
            "Resolving deltas: 100% (2/2), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5-FAaAQXkdKP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9b4c353c-1206-454f-d683-d462e8aee668"
      },
      "source": [
        "%cd /content/turbo-invention\n",
        "# insira o nome do seu repositório"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/turbo-invention\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "waxn4B2UDHyl"
      },
      "source": [
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "finLQoyyGVmk"
      },
      "source": [
        "## 2\\. Preço da gasolina"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7dJne-O92n2v"
      },
      "source": [
        "O código abaixo gera um arquivo com o preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O_uRYGzqy8OV"
      },
      "source": [
        "> **Nota**: Este arquivo é o mesmo do exercício do módulo anterior."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uhvy1LG31n1A",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1108c121-f908-4db5-a2e0-25ef1fa407d9"
      },
      "source": [
        "%%writefile gasolina.csv\n",
        "dia,venda\n",
        "1,5.11\n",
        "2,4.99\n",
        "3,5.02\n",
        "4,5.21\n",
        "5,5.07\n",
        "6,5.09\n",
        "7,5.13\n",
        "8,5.12\n",
        "9,4.94\n",
        "10,5.03"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing gasolina.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lcNhd195zE3t"
      },
      "source": [
        "### **2.1. Branch**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vK0ZbC9ozG4m"
      },
      "source": [
        "Crie uma branch chamada `develop` e aponte o context do `git` para a nova branch. Vamos simular uma atualização no exercício do módulo anterior."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hz6irIJszysS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bd108000-5cb9-4014-891d-c490c8d86115"
      },
      "source": [
        "# código de criação da branch develop\n",
        "%cd /content/turbo-invention\n",
        "!git branch develope\n",
        "!git checkout develope\n",
        "!echo \"Esta é uma atualização de exemplo.\" >> README.md\n",
        "!git add README.md\n",
        "!git commit -m \"Adicionada uma linha de exemplo ao README.md\"\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/turbo-invention\n",
            "fatal: A branch named 'develope' already exists.\n",
            "Already on 'develope'\n",
            "[develope 317e0d4] Adicionada uma linha de exemplo ao README.md\n",
            " 1 file changed, 1 insertion(+)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eun0qdii21WO"
      },
      "source": [
        "### **2.2. Desenvolvimento**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5MiknLIh2460"
      },
      "source": [
        "Gere uma gráfico de linha utilizando os dados do arquivo `gasolina.csv` com o dia no eixo `x`\n",
        " e o seu preço no eixo `y` utilizando os pacotes Python de sua preferência, como o Pandas e o Seaborn. Salve o gráfico no arquivo `gasolina.png` e o seu código Python de geração no arquivo `gasolina.py`."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8B3QgjlpzYdI"
      },
      "source": [
        "> **Nota**: Este gráfico deve alguns elementos diferente do anterior, como título, legenda, etc."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PPzewPcD3Z8n",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 569
        },
        "outputId": "5a5790a1-51ec-4819-b5d8-b79d8ee39961"
      },
      "source": [
        "# código de geração do gráfico\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Ler o arquivo CSV\n",
        "data = pd.read_csv('gasolina.csv')\n",
        "\n",
        "# Criar o gráfico de linha\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.lineplot(data=data, x='dia', y='venda', marker='o') # Changed 'preco' to 'venda'\n",
        "\n",
        "# Adicionar título e rótulos\n",
        "plt.title('Preço da Gasolina por Dia', fontsize=14)\n",
        "plt.xlabel('Dia', fontsize=12)\n",
        "plt.ylabel('Preço (R$)', fontsize=12)\n",
        "plt.legend(['Preço da Gasolina'], loc='upper left')\n",
        "\n",
        "# Salvar o gráfico\n",
        "plt.savefig('gasolina.png')\n",
        "\n",
        "# Mostrar o gráfico\n",
        "plt.show()\n"
      ],
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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hg0bMHHiRPz888+YPn36dWcioi5MJCKiNktLSxMBiJMnT77ivtdee00EII4fP958DIAIQFywYIGo1+sbnX/69GlRoVCI/fv3F4uKihrdt3jxYhGAuHTpUvOxY8eOiTKZTAwICBDT0tIanW80GsWcnBzzx2+88YYIQLz77rtFo9FoPn7kyBFRpVKJbm5uokajuebnu3PnThGA2L9/f7GystJ8PDs7W/Ty8hIBiPfdd1+jx6Smpl7xPDqdTrzxxhtFuVwuZmRkXPN14+LiRADi6NGjr3luU7Kzs8W6urorjpu+Lt9884352MaNG0UA4tNPP33F+RUVFWJtba354wULFogAxIULFzY677fffhMBiJGRkaLBYDAff/3110UA4s6dOxudD0AcO3Zso2P33XefCEAMCwsTc3NzzccLCwtFNzc30dnZudHnVFZWJhYXF1+R+c8//xRlMpn497///Yr7mmL6HgMQV6xY0ei+FStWiADEW265xXzMYDCIERERIgBxy5Ytjc5//vnnRQDi3/72t0bHQ0JCzP9uqqurW5RLFEVx5cqVIgBx8eLFVz3v3nvvFQGIX375pflYc1/7pn4+c3NzxYCAADEqKqrF2YiImsJphERE7SA5ORmLFi3CokWL8Pzzz2PMmDF48803oVarG40+AIBKpcJ7770HuVze6Phnn30GvV6P//znP/D09Gx03wsvvABvb2+sXbu20flGoxFvv/02QkNDG50vCAICAgLMH3/99ddQKpVYsmRJo5G2mJgY3HfffSgrK8OGDRuu+XmuXr0aAPDaa6/B0dHRfDwwMBBPPfVUk48JCwu74phCocDDDz8Mg8HQoula+fn5ANDoc7qc6Wt/+e1ygYGBjUYETR5//HEAaLKDob29/RXHnJycYGdnBwDQarVYu3YtPD098corrzQ676abbsKNN96I5OTkVk/T/KtXX30V/v7+5o+9vLwwffp0VFRU4Pz58+bjrq6u8PDwuOLx48ePR+/evVvdpTE6OhoPPPBAo2MPPPAAoqKi8Ntvv6GwsBAAsG/fPqSkpGDq1KmYPHlyo/Nfe+01eHh44Ntvv4VWq73iNd57770mv87Xy/RzUlRUdM1zm/r59Pf3x6xZs5CUlISMjIx2z0dEXQenERIRtYOUlBS88cYbAAClUglfX1/cddddeOmll66YxhQWFtbkQv3ExEQA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Mm666SbccccdCAkJQUJCAnbt2oWIiAgsWbKkXT/X7du3o7a2FkD9vmjZ2dnYvXs3cnJy4OHhgTVr1mDixInXfJ6HH34YK1euxKxZszB79mx4enoiMTERR44cwc0334zffvutXXMTURckXdd5IiLrd7V9tpqCJvZT+qsDBw6Id955pxgQECAqlUrRy8tLHDhwoPjSSy+JZ8+eveL8nTt3irfccovo7u4uAhDd3d3FWbNmifv27Wt0XmVlpfjqq6+K0dHR5r21pk6dKu7Zs6fFn68oiqJerxcXL14shoeHiyqVSgwPDxf/+c9/isnJyc3uszVr1izR29tbdHBwEIcMGSJ+99135v2cXn/99Va9fnV1tfjxxx+LEydOFH18fESFQiE6OTmJPXv2FBcsWCBu27btisdUVFSIzz77rBgaGira2dmJUVFR4ltvvSVqtdorvidnzpwRn3rqKTEmJkb09PQU7ezsxPDwcPG+++4TT58+fcVzFxYWik8++aQYEhJi/n7dfvvt4smTJ684ty37bP11D7XmnsdoNIorVqwQe/fuLarVatHPz0+8//77xYKCAnHs2LFiS//kX/592bNnjzh27FjR0dFRdHFxEWfOnCkmJSU1+bgTJ06It99+u+jl5SUqlUoxJCREfOqpp8TCwsIrzg0JCRFDQkJalOdypn22TDdBEEQnJycxNDRUnDZtmvif//xHLCkpafKxzX3td+7cKY4cOVJ0dnYW3dzcxJtuukk8fPhws+cTEbWGIIqXzSchIiKrNn/+fDg4OODTTz+VOgpZqV27dmH8+PF4/fXXr9ivjIiIWodrtoiIbMhtt92GL7/88oq9rIiIiKjzcc0WEZENePbZZ2FnZ4ctW7ZAp9Nd0UWOiIiIOh+LLSIiG5CRkYHffvsNzs7OeO+991q1DxURERF1DK7ZIiIiIiIi6gBcs0VERERERNQBWGwRERERERF1AK7ZagGj0Yjc3Fw4Oztfczd6IiIiIiKyXaIooqKiAgEBAdfcuJ7FVgvk5uYiKChI6hhERERERGQhsrKy0K1bt6uew2KrBUxdvbKysuDi4iJxGiIiIiIikopGo0FQUFCLOv+y2GoB09RBFxcXFltERERERNSi5UVskEFERERERNQBWGwRERERERF1ABZbREREREREHYBrttqJKIrQ6/UwGAxSRyG6JrlcDoVCwa0M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NLTR193f3x8FBQXmj5OSkvDaa69h//79KCoqgtFoBFA/bZPFVuep0eqxIi4Vy3YkmY+ZpgUDwENjwznCRURE1IXwr34HEAShxW+oarR6LIgNa/TmzGRBbFiHTj8aP348li9fDpVKhYCAgEajPED9yNblKisrMWjQIPzvf/+74rm8vb0lm6723Xff4bnnnsO///1vjBgxAs7OzvjXv/6F/fv3N/uYqKgo7N27FzqdDkqlEgDg5uYGNzc3ZGdnNzr3ueeew7Zt27B06VJERkbC3t4et99+u7lpiLOzM44cOYJdu3bhjz/+wGuvvYZFixZddV1Wa5kymgiCYC6oAGDatGkICQnB559/joCAABiNRvTp08cmG5tYMrlMdtVpwY+Nj+zkRERERCQlLuaQmL1KgUfHReCpCVFwsa8vdlzsFXhqQhQeHRfRoVfBHR0dERkZieDg4CsKraYMHDgQSUlJ8PHxQWRkZKObq6srnJ2dERoaih07djT5+J49eyIrKwtZWVnmY2fOnEFZWRl69erV7GNOnDiB2tpa87HExMRG5+zbtw+xsbF49NFHERMTg8jIyGs2h5g7dy4qKyvx6aefXvPz3rdvH+bPn4+ZM2eib9++8PPzu6IpiEKhwMSJE/Hee+/hxIkTSE9Px59//omIiAioVCrzujWgfu3bwYMHm/2cW6u4uBjnz5/HK6+8ggkTJqBnz54oLS1tl+em1qmo1V11WnBFra6TExEREZGUOLJlAeyUcjw0NhyPjY9stKDe0tZ33H333fjXv/6F6dOn480330S3bt2QkZGBn3/+GS+88AK6deuGRYsW4eGHH4aPjw+mTp2KiooK7Nu3D0888QQmTpyIvn374u6778aHH34IvV6PRx99FGPHjsXgwYObfM277roLL7/8Mh544AEsXLgQ6enpWLp0aaNzoqKisHr1amzduhVhYWFYs2YNDh48iLCwsGY/lxEjRuDZZ5/Fs88+i4yMDNx2220ICgpCXl4evvzySwiCYB6pi4qKws8//4xp06ZBEAS8+uqrjUaVNm3ahNTUVIwZMwbu7u7YvHkzjEYjunfvDkdHRzzyyCN4/vnn4eHhgeDgYLz33nuorq7G/fff3w7fFcDd3R2enp7473//C39/f2RmZuKll15ql+em1nFWK686LdhZrWziUURERGSrOLJlIRxUCqgUMng62UGl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C97Odiir1iHuQmGHvx4RERF1DBZbRETXkF9ei+SCSggCMCK844stuUzA9P71e25t4FRCIiIiq8Vii4joGuJT6ke1+gW6wtVB2SmvaepKuO3sRWhqdZ3ymkRERNS+WGwREV1DZ7R8/6veAS6I8nGCVm/ElpP5nfa6RERE1H5YbBERXYUoipdtZtx5xZYgCObRLXYlJCIisk4stoiIriKlsBIXNXWwU8gwKMS9U197+oD6dVuJacXILavp1NcmIiKi68dii4joKvYm1Y9qDQn1gFop79TX7ubugKFhHhBFYOPx3E59bSIiIrp+LLaIiK5iX0oxgM6dQng5055b7EpIRERkfVhsERE1Q28wIrGh2OqM/bWaclMff6jkMpzLr8DZPI0kGYiIiKhtWGwRETXjRE45Kur0cLVXoleAiyQZXB2UuKGHDwCObhEREVkbFltERM3Y17BeKzbCE3KZIFkOU1fCX47lwmAUJctBRERErcNii4ioGVLsr9WU8T284aJWIF9Ti/2pxZJmISIiopZjsUVE1IRqrR5HMksBSLdey8ROIcfN/erbwHPPLSIiIuvBYouIqAkH00uhM4gIdLNHiKeD1HHMXQl/P5WPWp1B4jRERETUEiy2iIiasK9hCuGoSC8IgnTrtUwGh7gj0M0elXV6bD97Ueo4RERE1AIstoiImmDazDg20lPiJPVkMgEzYuqnErIrIRERkXVgsUVE9BfFlXU407CnVWyEtOu1LjdjQP1Uwl3nC1FSpZU4DREREV0Liy0ior+Ib9jIuIefM7yd7SROc0mUrzP6BLpAbxTx24lcqeMQERHRNbDYIiL6i/iUS+u1LI1pdItdCYmIiCwfiy0ior8w768VZXnF1q39AyATgCOZZcgorpI6DhEREV0Fiy0iostkFlcjq6QGCpmAoaEeUse5go+L2rzJ8oajnEpIRERkyVhsERFdxjSqNTDYHY52ConTNM2059aGYzkQRVHiNERERNQcFltERJcx7a810gLXa5lM7u0He6UcaUVVOJ5dLnUcIiIiagaLLSKiBkajeKk5RpRl7K/VFEc7BSb39gXAPbeIiIgsGYstIqIGZ/I0KK3WwclOgX7d3KSOc1UzGqYS/no8FzqDUeI0RERE1BQWW0REDUxTCIeFeUApt+xfj6MiveDlpEJxlRZ7k4qkjkNERERNsOx3E0REnWiv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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T51dv46X3YoT"
      },
      "source": [
        "### **2.3. Git**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iyb6rFFX3YoU"
      },
      "source": [
        "Utilizando os comandos do `git`, adicione e \"commite\" os arquivos gerados (base, código Python e gráfico) na branch `develop`."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tRAunRfR4RfG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7c76df99-70c3-47cd-fabc-07b273b41f53"
      },
      "source": [
        "# comandos git para adicionar e commitar os arquivos\n",
        "# Certifique-se de estar na branch develope\n",
        "!git checkout develope\n",
        "!git add .\n",
        "\n"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A\tbase.txt\n",
            "A\tgasolina.csv\n",
            "A\tturbo-invention\n",
            "A\tturbo-invention.git\n",
            "Already on 'develope'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ozAPHQJu4P00"
      },
      "source": [
        "### **2.4. Github**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2JkFXRdW4P01"
      },
      "source": [
        "Utilizando os comandos do `git`, envie o seu commit para o GitHub."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xEKWMYH75FfC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5a80b264-13d0-4be3-fb59-15a34b304111"
      },
      "source": [
        "# comandos git para enviar o commit para o GitHub\n",
        "\n",
        "# Navegue até o diretório do repositório\n",
        "!cd /content/turbo-invention\n",
        "\n",
        "# Certifique-se de estar na branch develop\n",
        "!git checkout develope\n",
        "\n",
        "# Adicione os arquivos ao staging area\n",
        "!git add /content/turbo-invention/base.txt\n",
        "!git add /content/turbo-invention/hello.py\n",
        "!git add /content/turbo-invention/gasolina.png\n",
        "!git add /content/turbo-invention/gasolina.csv\n",
        "# Commit com uma mensagem descritiva\n",
        "!git commit -m \"Adiciona arquivos gerados: base, código Python e gráfico\"\n",
        "# Adicione o repositório remoto (caso ainda não tenha feito isso)\n",
        "!git remote add origin https://github.com/EDVADMBD/turbo-invention\n",
        "!git push -u  /content/turbo-invention\n",
        "\n",
        "\n"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A\tbase.txt\n",
            "A\tgasolina.csv\n",
            "A\tturbo-invention\n",
            "A\tturbo-invention.git\n",
            "Already on 'develope'\n",
            "[develope cfc161d] Adiciona arquivos gerados: base, código Python e gráfico\n",
            " 4 files changed, 12 insertions(+)\n",
            " create mode 100644 base.txt\n",
            " create mode 100644 gasolina.csv\n",
            " create mode 160000 turbo-invention\n",
            " create mode 100644 turbo-invention.git\n",
            "error: remote origin already exists.\n",
            "Branch 'develope' set up to track remote branch 'develope' from '/content/turbo-invention'.\n",
            "Everything up-to-date\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HX7eUrz90DoF"
      },
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fM_de4pA0D54"
      },
      "source": [
        "### **2.5. Pull Request e Merge**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w9byTlNc0D55"
      },
      "source": [
        "No GitHub, crie um *pull request* (PR) para enviar o código da branch de `develop` para a branch `main`. Ainda na plataforma online, confira as atualizações, aprove o PR e realize o *merge*."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git checkout -b develope\n",
        "!git push"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lkael_00_xMw",
        "outputId": "152c93a0-dcd9-42d5-93d1-6dc3f8503434"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: A branch named 'develope' already exists.\n",
            "Everything up-to-date\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "As3enQc2GVm1"
      },
      "source": [
        "---"
      ]
    }
  ]
}