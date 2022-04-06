{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.3"
    },
    "colab": {
      "name": "Python_para_Data_Science_Pandas.ipynb",
      "provenance": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/VRammos/python_tests/blob/main/Python_para_Data_Science_Pandas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W4bTJkJED0-t"
      },
      "source": [
        "# <font color=green> PYTHON PARA DATA SCIENCE - PANDAS\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GOEcCc62D0-x"
      },
      "source": [
        "# <font color=green> 1. INTRODUÇÃO AO PYTHON\n",
        "---"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hello Word!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kuBX8PO7s2IY",
        "outputId": "d21721b3-2023-47be-fddc-d6971a6c21ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello Word!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oGvoOJ-XD0-y"
      },
      "source": [
        "# 1.1 Introdução"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fam3BM0aD0-z"
      },
      "source": [
        "> Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares. \n",
        ">\n",
        "> Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assundo é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6kH5DY-vD0-1"
      },
      "source": [
        "# 1.2 Instalação e ambiente de desenvolvimento"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BTpm79I2D0-2"
      },
      "source": [
        "### Instalação Local\n",
        "\n",
        "### https://www.python.org/downloads/\n",
        "### ou\n",
        "### https://www.anaconda.com/distribution/"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AuPS_XwRD0-3"
      },
      "source": [
        "### Google Colaboratory\n",
        "\n",
        "### https://colab.research.google.com"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4rUYsPrXD0-4"
      },
      "source": [
        "### Verificando versão"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PgTCVRB2D0-5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "38ca3a47-7c38-4986-db6d-eac50a71cd1e"
      },
      "source": [
        "!python -V"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Python 3.7.13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lTtI6so4D0-9"
      },
      "source": [
        "# 1.3 Trabalhando com dados"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E_n4FUUWD0-9"
      },
      "source": [
        "import pandas as pd\n",
        "pd.set_option('display.max_rows', 10) #muda o numero max de linhas"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Kq-JdRHFD0-_"
      },
      "source": [
        "dataset = pd.read_csv('db.csv', sep = ';') #o sep cria a linha certa de cada dado"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "mOV1rCA6D0_A",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "outputId": "ca801275-5513-44df-bf65-5b8f17cd569c"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                      Nome                  Motor   Ano  Quilometragem  \\\n",
              "0            Jetta Variant        Motor 4.0 Turbo  2003        44410.0   \n",
              "1                   Passat           Motor Diesel  1991         5712.0   \n",
              "2                 Crossfox        Motor Diesel V8  1990        37123.0   \n",
              "3                      DS5        Motor 2.4 Turbo  2019            NaN   \n",
              "4         Aston Martin DB4        Motor 2.4 Turbo  2006        25757.0   \n",
              "..                     ...                    ...   ...            ...   \n",
              "253           Phantom 2013               Motor V8  2014        27505.0   \n",
              "254  Cadillac Ciel concept               Motor V8  1991        29981.0   \n",
              "255             Classe GLK  Motor 5.0 V8 Bi-Turbo  2002        52637.0   \n",
              "256       Aston Martin DB5           Motor Diesel  1996         7685.0   \n",
              "257                  Macan        Motor Diesel V6  1992        50188.0   \n",
              "\n",
              "     Zero_km                                         Acessórios      Valor  \n",
              "0      False  ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "1      False  ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "2      False  ['Piloto automático', 'Controle de estabilidad...   72832.16  \n",
              "3       True  ['Travas elétricas', '4 X 4', 'Vidros elétrico...  124549.07  \n",
              "4      False  ['Rodas de liga', '4 X 4', 'Central multimídia...   92612.10  \n",
              "..       ...                                                ...        ...  \n",
              "253    False  ['Controle de estabilidade', 'Piloto automátic...   51759.58  \n",
              "254    False  ['Bancos de couro', 'Painel digital', 'Sensor ...   51667.06  \n",
              "255    False  ['Rodas de liga', 'Controle de tração', 'Câmbi...   68934.03  \n",
              "256    False  ['Ar condicionado', '4 X 4', 'Câmbio automátic...  122110.90  \n",
              "257    False  ['Central multimídia', 'Teto panorâmico', 'Vid...   90381.47  \n",
              "\n",
              "[258 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e15dff45-1615-4c69-ab34-2d05e8358a62\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>DS5</td>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Aston Martin DB4</td>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>253</th>\n",
              "      <td>Phantom 2013</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2014</td>\n",
              "      <td>27505.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Piloto automátic...</td>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>254</th>\n",
              "      <td>Cadillac Ciel concept</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>1991</td>\n",
              "      <td>29981.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Painel digital', 'Sensor ...</td>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>255</th>\n",
              "      <td>Classe GLK</td>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2002</td>\n",
              "      <td>52637.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Controle de tração', 'Câmbi...</td>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>256</th>\n",
              "      <td>Aston Martin DB5</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>257</th>\n",
              "      <td>Macan</td>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>1992</td>\n",
              "      <td>50188.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Vid...</td>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 7 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e15dff45-1615-4c69-ab34-2d05e8358a62')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e15dff45-1615-4c69-ab34-2d05e8358a62 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e15dff45-1615-4c69-ab34-2d05e8358a62');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 153
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5D739PzJD0_B",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3a713065-10e5-4b8c-cde7-6607815c5cf1"
      },
      "source": [
        "dataset.dtypes"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Nome              object\n",
              "Motor             object\n",
              "Ano                int64\n",
              "Quilometragem    float64\n",
              "Zero_km             bool\n",
              "Acessórios        object\n",
              "Valor            float64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 154
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r_qUf16LD0_D",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "outputId": "8baeef8a-3e89-43e2-e33d-14795a09d09f"
      },
      "source": [
        "dataset[['Quilometragem', 'Valor']].describe() #vê informações especificas e descreve cada info"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       Quilometragem          Valor\n",
              "count     197.000000     258.000000\n",
              "mean    58278.421320   98960.513101\n",
              "std     35836.733259   29811.932305\n",
              "min       107.000000   50742.100000\n",
              "25%     27505.000000   70743.512500\n",
              "50%     55083.000000   97724.380000\n",
              "75%     90495.000000  124633.302500\n",
              "max    119945.000000  149489.920000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a84ca3ab-7d0e-44cb-b7b7-fd03c9633e59\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>197.000000</td>\n",
              "      <td>258.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>58278.421320</td>\n",
              "      <td>98960.513101</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>35836.733259</td>\n",
              "      <td>29811.932305</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>107.000000</td>\n",
              "      <td>50742.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>27505.000000</td>\n",
              "      <td>70743.512500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>55083.000000</td>\n",
              "      <td>97724.380000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>90495.000000</td>\n",
              "      <td>124633.302500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>119945.000000</td>\n",
              "      <td>149489.920000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a84ca3ab-7d0e-44cb-b7b7-fd03c9633e59')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a84ca3ab-7d0e-44cb-b7b7-fd03c9633e59 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a84ca3ab-7d0e-44cb-b7b7-fd03c9633e59');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 155
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0R-_7PH5D0_E",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c621fdaa-a111-4338-abbb-bcc72b088963"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 258 entries, 0 to 257\n",
            "Data columns (total 7 columns):\n",
            " #   Column         Non-Null Count  Dtype  \n",
            "---  ------         --------------  -----  \n",
            " 0   Nome           258 non-null    object \n",
            " 1   Motor          258 non-null    object \n",
            " 2   Ano            258 non-null    int64  \n",
            " 3   Quilometragem  197 non-null    float64\n",
            " 4   Zero_km        258 non-null    bool   \n",
            " 5   Acessórios     258 non-null    object \n",
            " 6   Valor          258 non-null    float64\n",
            "dtypes: bool(1), float64(2), int64(1), object(3)\n",
            "memory usage: 12.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "htjoBLwiD0_F"
      },
      "source": [
        "# <font color=green> 2. TRABALHANDO COM TUPLAS\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MZH5_QnYD0_G"
      },
      "source": [
        "# 2.1 Criando tuplas\n",
        "\n",
        "Tuplas são sequências imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. Podem ser construídas de várias formas:\n",
        "```\n",
        "- Utilizando um par de parênteses: ( )\n",
        "- Utilizando uma vírgula à direita: x,\n",
        "- Utilizando um par de parênteses com itens separados por vírgulas: ( x, y, z )\n",
        "- Utilizando: tuple() ou tuple(iterador)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xzcs9fzeD0_G",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5ee0f0d2-5ce5-478e-c98e-5b8b9cac7650"
      },
      "source": [
        "()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "()"
            ]
          },
          "metadata": {},
          "execution_count": 157
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qJq7a2qTD0_I",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2d557a5c-4c1e-4e82-f969-69cdecf3c68f"
      },
      "source": [
        "1, 2, 3"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1, 2, 3)"
            ]
          },
          "metadata": {},
          "execution_count": 158
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sg7LdvptD0_J",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "16291a6f-bdd6-4eba-da6b-099b0577fdcb"
      },
      "source": [
        "nome = 'Passat'\n",
        "valor = 153000\n",
        "(nome, valor)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Passat', 153000)"
            ]
          },
          "metadata": {},
          "execution_count": 159
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XSSMebXjD0_K",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "861077e4-d05c-4aa9-bc49-710a43e67e75"
      },
      "source": [
        "nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])\n",
        "nomes_carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Jetta Variant', 'Passat', 'Crossfox', 'DS5')"
            ]
          },
          "metadata": {},
          "execution_count": 160
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dpkdzrzRD0_M",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f1da994f-7a7d-44e5-f3ce-a67610882d99"
      },
      "source": [
        "type(nomes_carros)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tuple"
            ]
          },
          "metadata": {},
          "execution_count": 161
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iKUY2DOUD0_N"
      },
      "source": [
        "# 2.2 Seleções em tuplas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hBEeAM7_D0_N",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6feec24b-474d-4471-be1b-3d699bd1e967"
      },
      "source": [
        "nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')\n",
        "nomes_carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Jetta Variant', 'Passat', 'Crossfox', 'DS5')"
            ]
          },
          "metadata": {},
          "execution_count": 162
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-mx_1E_tD0_P",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "aa1afb70-0a80-4ea9-c9a1-f814527f277e"
      },
      "source": [
        "nomes_carros[0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Jetta Variant'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 163
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LMhyqnFID0_Q",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "0fa6a1ca-79ef-4d45-8f6b-726376b19485"
      },
      "source": [
        "nomes_carros[1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Passat'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 164
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6btHff4BD0_T",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "ea890c64-04c4-4ef8-e9ff-bf096de3200b"
      },
      "source": [
        "nomes_carros[-1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'DS5'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 165
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K_Dc12xBD0_U",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "391a908f-412c-4279-aa62-f6baeb4236ed"
      },
      "source": [
        "nomes_carros[1:3]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Passat', 'Crossfox')"
            ]
          },
          "metadata": {},
          "execution_count": 166
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zvrWYkkeD0_W",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ea8292d6-d76d-49f4-ae36-38359fa1dbab"
      },
      "source": [
        "nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))\n",
        "nomes_carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))"
            ]
          },
          "metadata": {},
          "execution_count": 167
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Dw7tbM2ED0_Z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eac86d04-42cb-45f7-8c0d-1aea376b2f52"
      },
      "source": [
        "nomes_carros[-1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Fusca', 'Gol', 'C4')"
            ]
          },
          "metadata": {},
          "execution_count": 168
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SAMD3BtXD0_b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "a833ff0d-6434-406b-be86-0cf47d035fc2"
      },
      "source": [
        "nomes_carros[-1][1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Gol'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 169
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KLMxh4-0D0_c"
      },
      "source": [
        "# 2.3 Iterando em tuplas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K53elKsYD0_c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ec19be6c-d4bc-46e7-a326-e7829c10dc10"
      },
      "source": [
        "nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')\n",
        "nomes_carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Jetta Variant', 'Passat', 'Crossfox', 'DS5')"
            ]
          },
          "metadata": {},
          "execution_count": 170
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "igZhZ5zdD0_d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "dadde30c-148f-45f0-9241-439125a81ff4"
      },
      "source": [
        "for item in nomes_carros:\n",
        "  print(item)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jetta Variant\n",
            "Passat\n",
            "Crossfox\n",
            "DS5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AOBjxBk8D0_f"
      },
      "source": [
        "### Desempacotamento de tuplas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UoEFnumhD0_f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "666129b6-010c-4d2a-e015-c9552d696666"
      },
      "source": [
        "nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')\n",
        "nomes_carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Jetta Variant', 'Passat', 'Crossfox', 'DS5')"
            ]
          },
          "metadata": {},
          "execution_count": 172
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AaCLcNYTD0_g"
      },
      "source": [
        "carro_1, carro_2, carro_3, carro_4 = nomes_carros #relaciona o valor com dados na tupla(array)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TA71S9egD0_h",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 328
        },
        "outputId": "c57fef5d-2839-4936-b7b7-965943881134"
      },
      "source": [
        "carro_1"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Jetta Variant'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 174
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CHoJ034MD0_i",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 201
        },
        "outputId": "a4a45562-673f-474f-cc6b-e9536a2b7e18"
      },
      "source": [
        "carro_2"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Passat'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 175
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oxJrOuCSD0_j",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 242
        },
        "outputId": "bddd4da0-ad6a-4e6f-973f-1623a44011d5"
      },
      "source": [
        "carro_3"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Crossfox'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 176
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BbR9sB4BD0_k",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 146
        },
        "outputId": "024bd1cd-7123-47f6-8939-312d7cfe2d74"
      },
      "source": [
        "carro_4"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'DS5'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 177
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aZvokrjPD0_m"
      },
      "source": [
        "_, A, _, B= nomes_carros #Escolhendo valores especificos na tupla"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wZXDbVg0D0_o",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 201
        },
        "outputId": "29e0dc81-9ede-4acf-bba2-5948cc35d7d5"
      },
      "source": [
        "A"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Passat'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 179
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aWgDMBXiD0_p",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 146
        },
        "outputId": "e69ce429-28f5-4474-e610-12199c6d40f9"
      },
      "source": [
        "B"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'DS5'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 180
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OdpgNh-ND0_q"
      },
      "source": [
        "_, C, *_ = nomes_carros #para ignorar o resto da lista"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "upVYFnMdD0_r",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 201
        },
        "outputId": "249705bb-45f8-42c5-d71e-25772e34fe3d"
      },
      "source": [
        "C"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Passat'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 182
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "u85Aou8WD0_s"
      },
      "source": [
        "## *zip()*\n",
        "\n",
        "https://docs.python.org/3.6/library/functions.html#zip"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PaC2oXGED0_t",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8b76822a-2f19-4971-cad5-a1b5ab895670"
      },
      "source": [
        "carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']\n",
        "carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Jetta Variant', 'Passat', 'Crossfox', 'DS5']"
            ]
          },
          "metadata": {},
          "execution_count": 183
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_02O1VnHD0_u",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e5c4c37-3c39-42b4-f624-37403aaef35f"
      },
      "source": [
        "valores = [88078.64, 106161.94, 72832.16, 124549.07]\n",
        "valores"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[88078.64, 106161.94, 72832.16, 124549.07]"
            ]
          },
          "metadata": {},
          "execution_count": 184
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "roQK5nYRD0_v",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "15803d14-3019-4013-e415-024b29053c20"
      },
      "source": [
        "list(zip(carros, valores)) #cria uma lista com os valores equivalentes em cada lista [0][1] e [1][1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('Jetta Variant', 88078.64),\n",
              " ('Passat', 106161.94),\n",
              " ('Crossfox', 72832.16),\n",
              " ('DS5', 124549.07)]"
            ]
          },
          "metadata": {},
          "execution_count": 185
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_WRxIRHrD0_w",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5cf2baf7-38ac-4cea-b4a1-c6bbc32358ec"
      },
      "source": [
        "for item in zip(carros, valores):\n",
        "  print(item)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('Jetta Variant', 88078.64)\n",
            "('Passat', 106161.94)\n",
            "('Crossfox', 72832.16)\n",
            "('DS5', 124549.07)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2zIuhIILD0_x",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e01b1de5-29af-4058-d809-3fcaa8435c82"
      },
      "source": [
        "for carro, valor in zip(carros, valores):\n",
        "  print(carro, ',', valor)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jetta Variant , 88078.64\n",
            "Passat , 106161.94\n",
            "Crossfox , 72832.16\n",
            "DS5 , 124549.07\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZJaL62IpD0_y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "84aeeb5e-e386-469b-c083-cf033e5fc0cd"
      },
      "source": [
        "for carro, valor in zip(carros, valores):\n",
        "  if (valor > 100000):\n",
        "    print(carro)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Passat\n",
            "DS5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xo76nR8rD0_0"
      },
      "source": [
        "# <font color=green> 3. TRABALHANDO COM DICIONÁRIOS\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wfWzOuztD0_0"
      },
      "source": [
        "# 3.1 Criando dicionários\n",
        "\n",
        "Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.\n",
        "\n",
        "Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido como chave (*key*) e o segundo como valor (*value*).\n",
        "\n",
        "```\n",
        "dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}\n",
        "```\n",
        "\n",
        "https://docs.python.org/3.6/library/stdtypes.html#typesmapping"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YIFVkWT6D0_1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a0d6f9b2-2bb9-483d-8f96-89503f977451"
      },
      "source": [
        "carros = ['Jetta Variant', 'Passat', 'Crossfox']\n",
        "carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Jetta Variant', 'Passat', 'Crossfox']"
            ]
          },
          "metadata": {},
          "execution_count": 189
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2LHiBn3-D0_2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2715bbc0-adee-4508-f0d5-93bdb14b19c6"
      },
      "source": [
        "valores = [88078.64, 106161.94, 72832.16]\n",
        "valores"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[88078.64, 106161.94, 72832.16]"
            ]
          },
          "metadata": {},
          "execution_count": 190
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YxLAx_sqD0_4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "05411d40-6ad7-4ead-d286-fb6fb059e45e"
      },
      "source": [
        "carros.index('Passat')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 191
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WITNWExID0_7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3335a74d-554d-49d9-9bff-333620bf8067"
      },
      "source": [
        "valores[carros.index('Passat')]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "106161.94"
            ]
          },
          "metadata": {},
          "execution_count": 192
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bHNqoDbTD0_8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c90292ad-aa6f-49df-bd7c-b5ed15f327ba"
      },
      "source": [
        "dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}\n",
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'Jetta Variant': 88078.64, 'Passat': 106161.94}"
            ]
          },
          "metadata": {},
          "execution_count": 193
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4FyQgmcAD0_9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4ec46cce-7f4f-49f3-ddfd-4dff711333fb"
      },
      "source": [
        "type(dados)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict"
            ]
          },
          "metadata": {},
          "execution_count": 194
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PQg-MLkGD0_-"
      },
      "source": [
        "### Criando dicionários com *zip()*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iB4Q_gbND0__",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "010ac2c9-c86b-4d52-acdd-594d80a737d5"
      },
      "source": [
        "list(zip(carros, valores))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('Jetta Variant', 88078.64), ('Passat', 106161.94), ('Crossfox', 72832.16)]"
            ]
          },
          "metadata": {},
          "execution_count": 195
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mIgZqdKKD1AA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c7de2864-6dd9-4b06-b74d-88b37447e71f"
      },
      "source": [
        "dados = dict(zip(carros, valores))\n",
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'Jetta Variant': 88078.64, 'Passat': 106161.94}"
            ]
          },
          "metadata": {},
          "execution_count": 196
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KYeRqavFD1AD"
      },
      "source": [
        "# 3.2 Operações com dicionários"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KzmWbEltD1AD"
      },
      "source": [
        "## *dict[ key ]*\n",
        "\n",
        "Retorna o valor correspondente à chave (*key*) no dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hFFDz6wKD1AD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "819ba28d-67b7-452f-f411-73c94b9dc0ed"
      },
      "source": [
        "dados['Passat'] # funciona como: map(obj/valor)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "106161.94"
            ]
          },
          "metadata": {},
          "execution_count": 197
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SWlE6VTBD1AE"
      },
      "source": [
        "## *key in dict*\n",
        "\n",
        "Retorna **True** se a chave (*key*) for encontrada no dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Iy88SxBtD1AE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6287531b-1d7f-4860-d6a4-e25cedb791cd"
      },
      "source": [
        "\"Passat\" in dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 198
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Oma56NkAD1AF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2152df5b-6cce-4132-c5cb-f875ed5b6e2a"
      },
      "source": [
        "'Fusca' in dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 199
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yS2U-_8gD1AG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "baa7cccb-9c9b-46f8-8343-694c4b447fed"
      },
      "source": [
        "\"Golf\" not in dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 200
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oWbWyDd0D1AI"
      },
      "source": [
        "## *len(dict)*\n",
        "\n",
        "Retorna o número de itens do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k08YkCc1D1AJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "18de76f9-3551-4a50-e565-b7f0566be32f"
      },
      "source": [
        "len(dados)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 201
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yYNqIHJBD1AK"
      },
      "source": [
        "## *dict[ key ] = value*\n",
        "\n",
        "Inclui um item ao dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5jj3i52bD1AK"
      },
      "source": [
        "dados[\"DS5\"] = 124549.07"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y6rso5hLD1AL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "08205e19-a1ec-4f78-9fe2-578744fda817"
      },
      "source": [
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.94}"
            ]
          },
          "metadata": {},
          "execution_count": 203
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_z0JySuqD1AL"
      },
      "source": [
        "## *del dict[ key ]*\n",
        "\n",
        "Remove o item de chave (*key*) do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PPfh6sfID1AM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f74fb5b1-e704-4d89-ee37-2d8b50f7b6e1"
      },
      "source": [
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.94}"
            ]
          },
          "metadata": {},
          "execution_count": 204
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BtjGpXtGD1AN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b8e303f5-ec7b-4f9e-8b73-ba0821fcbc1c"
      },
      "source": [
        "del dados['Passat']\n",
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64}"
            ]
          },
          "metadata": {},
          "execution_count": 205
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lQB40P9vV3ln",
        "outputId": "ab4480d1-427b-455d-c867-97ccd33beca8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64}"
            ]
          },
          "metadata": {},
          "execution_count": 206
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FodJVx5sD1AP"
      },
      "source": [
        "# 3.3 Métodos de dicionários"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7pqdPOkYD1AP"
      },
      "source": [
        "## *dict.update()*\n",
        "\n",
        "Atualiza o dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DUySYxKQD1AQ"
      },
      "source": [
        "dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64}"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DLsqp71cD1AR"
      },
      "source": [
        "dados.update({'Passat': 106161.95, 'Fusca': 150000})"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JLs5c0DeD1AR"
      },
      "source": [
        "## *dict.copy()*\n",
        "\n",
        "Cria uma cópia do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X9F7OB3eD1AS"
      },
      "source": [
        "dadosCopy = dados.copy()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v0rL0bveD1AS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "423c80cf-cab3-4a81-e9d5-fb29542baf39"
      },
      "source": [
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Fusca': 150000,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.95}"
            ]
          },
          "metadata": {},
          "execution_count": 210
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M-abRGGrD1AT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "af6996e5-b698-4140-82da-f220cd45d155"
      },
      "source": [
        "del dadosCopy['Fusca']\n",
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.95}"
            ]
          },
          "metadata": {},
          "execution_count": 211
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ETBD0TkND1AU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6e8020ca-641e-479e-93e6-2e866cb9c4a5"
      },
      "source": [
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Fusca': 150000,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.95}"
            ]
          },
          "metadata": {},
          "execution_count": 212
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mNODkmHCD1AV"
      },
      "source": [
        "## *dict.pop(key[, default ])*\n",
        "\n",
        "Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como *default* é retornado. Se o valor *default* não for fornecido e a chave não for encontrada no dicionário um erro será gerado."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_4QEPwScD1AW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a0aa9a03-f40d-4590-8301-cfebc65b533e"
      },
      "source": [
        "dadosCopy "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Jetta Variant': 88078.64,\n",
              " 'Passat': 106161.95}"
            ]
          },
          "metadata": {},
          "execution_count": 213
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hjh0MuymD1AX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "34197277-a9f4-440e-e7e6-9e9c325512ab"
      },
      "source": [
        "dadosCopy.pop('Passat') #É obrigatorio dar um argumento, não funciona sem"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "106161.95"
            ]
          },
          "metadata": {},
          "execution_count": 214
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f51rKjkuD1AX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6d4b4824-ed14-40c6-f84d-2e130cdfd343"
      },
      "source": [
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64}"
            ]
          },
          "metadata": {},
          "execution_count": 215
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ah4sZ7axD1AZ"
      },
      "source": [
        "# dadosCopy('Passat')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SJATRY8RD1Aa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 467
        },
        "outputId": "8a9d0021-bdb3-4c24-c695-fc2f8a7e020c"
      },
      "source": [
        "dadosCopy.pop('Passat', 'Chave não encontrada')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Chave não encontrada'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 217
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V36wHdzmD1Ab",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fa7dab7e-3540-4654-bb37-afb74eef46f3"
      },
      "source": [
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'DS5': 124549.07, 'Jetta Variant': 88078.64}"
            ]
          },
          "metadata": {},
          "execution_count": 218
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LJ0lQIrdD1Ac",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c842b394-259e-4e33-982e-ccb2443c7bd3"
      },
      "source": [
        "dadosCopy.pop('DS5', 'Chave não encontrada')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "124549.07"
            ]
          },
          "metadata": {},
          "execution_count": 219
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yKGu-fYkD1Ad",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1417a1c1-d25f-4c9f-86e7-4008dd341235"
      },
      "source": [
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'Jetta Variant': 88078.64}"
            ]
          },
          "metadata": {},
          "execution_count": 220
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q5J0R7d3D1Ag"
      },
      "source": [
        "## *dict.clear()*\n",
        "\n",
        "Remove todos os itens do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AvkP_8mND1Ag"
      },
      "source": [
        "dadosCopy.clear()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S69pMYboD1Ah",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c7e342b2-c63e-4ad4-ff94-bee6d4969c3b"
      },
      "source": [
        "dadosCopy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{}"
            ]
          },
          "metadata": {},
          "execution_count": 222
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QhoSRfPsD1Ai"
      },
      "source": [
        "# 3.4 Iterando em dicionários"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Fusca': 150000, 'Jeta Variant': 88078.64, 'Passat': 106161.95}\n",
        "dados"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jn60slPta4a3",
        "outputId": "5b598020-8d79-4b06-8aed-db79247600a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16,\n",
              " 'DS5': 124549.07,\n",
              " 'Fusca': 150000,\n",
              " 'Jeta Variant': 88078.64,\n",
              " 'Passat': 106161.95}"
            ]
          },
          "metadata": {},
          "execution_count": 223
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "E-agaqakD1Ai"
      },
      "source": [
        "## *dict.keys()*\n",
        "\n",
        "Retorna uma lista contendo as chaves (*keys*) do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qFADEYmBD1Aj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d4b301e8-ab81-4ce1-c5bb-3b0fb5010f05"
      },
      "source": [
        "dados.keys()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_keys(['Crossfox', 'DS5', 'Fusca', 'Jeta Variant', 'Passat'])"
            ]
          },
          "metadata": {},
          "execution_count": 224
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "niwh9AgDD1Aj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e4f8012-0b17-49eb-d152-bd49050b4527"
      },
      "source": [
        "for key in dados.keys():\n",
        "  print(dados[key])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "72832.16\n",
            "124549.07\n",
            "150000\n",
            "88078.64\n",
            "106161.95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qFj6Cc7dD1Ak"
      },
      "source": [
        "## *dict.values()*\n",
        "\n",
        "Retorna uma lista com todos os valores (*values*) do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nfpLxrQVD1Al",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6c1444d4-cfd7-4845-cc43-fb06ce04c916"
      },
      "source": [
        "dados.values()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_values([72832.16, 124549.07, 150000, 88078.64, 106161.95])"
            ]
          },
          "metadata": {},
          "execution_count": 226
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-NGRwX0AD1Al"
      },
      "source": [
        "## *dict.items()*\n",
        "\n",
        "Retorna uma lista contendo uma tupla para cada par chave-valor (*key-value*) do dicionário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q2I9_6YvD1Am",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2358223f-368f-4375-fcbc-159b9fbba4c9"
      },
      "source": [
        "dados.items()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_items([('Crossfox', 72832.16), ('DS5', 124549.07), ('Fusca', 150000), ('Jeta Variant', 88078.64), ('Passat', 106161.95)])"
            ]
          },
          "metadata": {},
          "execution_count": 227
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0j41ZqgQD1Am",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "aa3fd4c5-df8c-49ab-dc52-fc743afcb286"
      },
      "source": [
        "for item in dados.items():\n",
        "  print(item)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('Crossfox', 72832.16)\n",
            "('DS5', 124549.07)\n",
            "('Fusca', 150000)\n",
            "('Jeta Variant', 88078.64)\n",
            "('Passat', 106161.95)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OVY9rIwFD1An",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e7019a4f-c98d-431e-9946-12bd4308ce2b"
      },
      "source": [
        "for key, value in dados.items():\n",
        "  print(key, value)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Crossfox 72832.16\n",
            "DS5 124549.07\n",
            "Fusca 150000\n",
            "Jeta Variant 88078.64\n",
            "Passat 106161.95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ma2Ol8vcD1Ap",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "410a7983-6777-40fa-843d-cafe1fdd7cf8"
      },
      "source": [
        "for key, value in dados.items():\n",
        "  if (value> 100000):\n",
        "    print(key, value)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "DS5 124549.07\n",
            "Fusca 150000\n",
            "Passat 106161.95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-q3AlSg3D1Aq"
      },
      "source": [
        "# <font color=green> 4. FUNÇÕES E PACOTES\n",
        "---\n",
        "    \n",
        "Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5CfEcU58D1Aq"
      },
      "source": [
        "# 4.1 Built-in function\n",
        "\n",
        "A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.\n",
        "\n",
        "https://docs.python.org/3.6/library/functions.html"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DP7cmY7xD1Aq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ba7d99cb-5d19-455d-fede-174e2653f97b"
      },
      "source": [
        "dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}\n",
        "dados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': 72832.16, 'Jetta Variant': 88078.64, 'Passat': 106161.94}"
            ]
          },
          "metadata": {},
          "execution_count": 231
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5zAcGSCbD1Ar",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0de12d6b-2e5a-4044-9ad8-f7207d9b6f67"
      },
      "source": [
        "valores = []\n",
        "for valor in dados.values():\n",
        "  valores.append(valor)\n",
        "valores"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[88078.64, 106161.94, 72832.16]"
            ]
          },
          "metadata": {},
          "execution_count": 232
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jn0O3uXZD1Au",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d27f25af-e50c-4b19-96b4-a7be5ec56ec8"
      },
      "source": [
        "list(dados.values())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[88078.64, 106161.94, 72832.16]"
            ]
          },
          "metadata": {},
          "execution_count": 233
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zG9_jU_1D1At",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ac01a13f-eceb-4f39-ac32-da66e0475f47"
      },
      "source": [
        "soma = 0\n",
        "for valor in dados.values():\n",
        "  soma += valor\n",
        "soma"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "267072.74"
            ]
          },
          "metadata": {},
          "execution_count": 234
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lnUjKVnoD1Aw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "82fa4028-2dba-4306-bdf5-2d5e95d8c8e5"
      },
      "source": [
        "sum(dados.values())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "267072.74"
            ]
          },
          "metadata": {},
          "execution_count": 235
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": false,
        "id": "WdEuYXe2D1Ay",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "94478e5b-b326-4608-a5dd-298307981a6e"
      },
      "source": [
        "help(sum)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Help on built-in function sum in module builtins:\n",
            "\n",
            "sum(iterable, start=0, /)\n",
            "    Return the sum of a 'start' value (default: 0) plus an iterable of numbers\n",
            "    \n",
            "    When the iterable is empty, return the start value.\n",
            "    This function is intended specifically for use with numeric values and may\n",
            "    reject non-numeric types.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6w62Sl5ZD1A0"
      },
      "source": [
        "# 4.2 Definindo funções sem e com parâmetros"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OADZiBP2D1A0"
      },
      "source": [
        "### Funções sem parâmetros\n",
        "\n",
        "#### Formato padrão\n",
        "\n",
        "```\n",
        "def <nome>():\n",
        "    <instruções>\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uCkplEpQD1A0"
      },
      "source": [
        "def media():\n",
        "  valor = (1 + 2 + 3) / 3\n",
        "  print(valor)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fOCEGq5VD1A1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7ce77887-3c22-4377-c924-1b97443300ca"
      },
      "source": [
        "media()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PwSlYSVAD1A2"
      },
      "source": [
        "### Funções com parâmetros\n",
        "\n",
        "#### Formato padrão\n",
        "\n",
        "```\n",
        "def <nome>(<param_1>, <param_2>, ..., <param_n>):\n",
        "    <instruções>\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A3YnBUduD1A3"
      },
      "source": [
        "def media(number_1, number_2, number_3):\n",
        "  valor = (number_1 + number_2 + number_3) / 3\n",
        "  print(valor)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rGUZbRERD1A3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "59234b91-270f-4820-84ef-2e7ebb45afc7"
      },
      "source": [
        "media(1, 2, 3)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B9WDlRE7D1A5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "80edbf3f-8cf4-49cd-9d15-f4b143384fc7"
      },
      "source": [
        "media(23, 45, 67)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "45.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1HAy8OK_D1A6"
      },
      "source": [
        "def media(lista):\n",
        "  valor = sum(lista) / len(lista)\n",
        "  print(valor)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_CDa4oOfD1A6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1a63f621-1dae-42ed-b9b3-8709a8f2eaee"
      },
      "source": [
        "resultado = media([1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8zNYrmFbD1A9"
      },
      "source": [
        "# 4.3 Definindo funções que retornam valores"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J44K-dMOD1A9"
      },
      "source": [
        "### Funções que retornam um valor\n",
        "\n",
        "#### Formato padrão\n",
        "\n",
        "```\n",
        "def <nome>(<param_1>, <param_2>, ..., <param_n>):\n",
        "    <instruções>\n",
        "    return <resultado>\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-UG42RQJD1A9"
      },
      "source": [
        "def media(lista):\n",
        "  valor = sum(lista) / len(lista)\n",
        "  return valor"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VJwdvoT5D1A-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7f773f94-ecdd-4136-a2b8-6f13b0424173"
      },
      "source": [
        "media([1, 2, 3, 4, 5, 6, 7, 8])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.5"
            ]
          },
          "metadata": {},
          "execution_count": 245
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AgAeJkpND1A-"
      },
      "source": [
        "resultado = media([1, 2, 3, 4, 5, 6, 7, 8])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_r616TevD1A_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2514290d-aa59-4360-969e-ac527c5468a8"
      },
      "source": [
        "resultado"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.5"
            ]
          },
          "metadata": {},
          "execution_count": 247
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MQaK8GV5D1BA"
      },
      "source": [
        "### Funções que retornam mais de um valor\n",
        "\n",
        "#### Formato padrão\n",
        "\n",
        "```\n",
        "def <nome>(<param_1>, <param_2>, ..., <param_n>):\n",
        "    <instruções>\n",
        "    return (<resultado_1>, <resultado_2>, ..., <resultado_n>)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v0PUMegVD1BA"
      },
      "source": [
        "def media(lista):\n",
        "  valor = sum(lista) / len(lista)\n",
        "  return (valor, len(lista))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ys-etom8D1BA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "810d0739-9d09-4949-dccf-cb4b93903e73"
      },
      "source": [
        "media([1, 2, 3, 4, 5, 6, 7, 8])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4.5, 8)"
            ]
          },
          "metadata": {},
          "execution_count": 249
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LERrvkMHD1BC"
      },
      "source": [
        "resultado, n = media([1, 2, 3, 4, 5, 6, 7, 8])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sqoFOWSsD1BC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ce124df7-0461-4ee4-8edb-ccc8978c06d1"
      },
      "source": [
        "resultado"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.5"
            ]
          },
          "metadata": {},
          "execution_count": 251
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NdB_Jyw_D1BD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "16bb04c6-49c5-41b0-dabf-fab7de1be843"
      },
      "source": [
        "n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8"
            ]
          },
          "metadata": {},
          "execution_count": 252
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados = {\n",
        "    'Crossfox': {'km': 35000, 'ano': 2005}, \n",
        "    'DS5': {'km': 17000, 'ano': 2015}, \n",
        "    'Fusca': {'km': 130000, 'ano': 1979}, \n",
        "    'Jetta': {'km': 56000, 'ano': 2011}, \n",
        "    'Passat': {'km': 62000, 'ano': 1999}\n",
        "}"
      ],
      "metadata": {
        "id": "mwnrJOC02W7B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Atualiza a km atual\n",
        "def km_media(dataset, ano_atual):\n",
        "    result = {}\n",
        "    for item in dataset.items():\n",
        "        media = item[1]['km'] / (ano_atual - item[1]['ano'])\n",
        "        item[1].update({ 'km_media': media })\n",
        "        result.update({ item[0]: item[1] })\n",
        "    return result"
      ],
      "metadata": {
        "id": "X_aZQXXe2ZTg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "km_media(dados, 2019)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BlRXtwh12_vt",
        "outputId": "4f9be9a4-bc81-4cfc-cd1e-84e1fde80000"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'Crossfox': {'ano': 2005, 'km': 35000, 'km_media': 2500.0},\n",
              " 'DS5': {'ano': 2015, 'km': 17000, 'km_media': 4250.0},\n",
              " 'Fusca': {'ano': 1979, 'km': 130000, 'km_media': 3250.0},\n",
              " 'Jetta': {'ano': 2011, 'km': 56000, 'km_media': 7000.0},\n",
              " 'Passat': {'ano': 1999, 'km': 62000, 'km_media': 3100.0}}"
            ]
          },
          "metadata": {},
          "execution_count": 255
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uQ5lNnKrD1BD"
      },
      "source": [
        "# <font color=green> 5. PANDAS BÁSICO\n",
        "---\n",
        "\n",
        "**versão: 0.25.2**\n",
        "  \n",
        "Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.\n",
        "\n",
        "\n",
        "## Estruturas de Dados\n",
        "\n",
        "### Series\n",
        "\n",
        "Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de **index**. A forma básica de criação de uma Series é a seguinte:\n",
        "\n",
        "\n",
        "```\n",
        "    s = pd.Series(dados, index = index)\n",
        "```\n",
        "\n",
        "O argumento *dados* pode ser um dicionário, uma lista, um array Numpy ou uma constante.\n",
        "\n",
        "### DataFrames\n",
        "\n",
        "DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.\n",
        "\n",
        "\n",
        "```\n",
        "    df = pd.DataFrame(dados, index = index, columns = columns)\n",
        "```\n",
        "\n",
        "O argumento *dados* pode ser um dicionário, uma lista, um array Numpy, uma Series e outro DataFrame.\n",
        "\n",
        "**Documentação:** https://pandas.pydata.org/pandas-docs/version/0.25/"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2qa7RC03D1BD"
      },
      "source": [
        "# 5.1 Estruturas de dados"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4QyFDeS4D1BD"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kIey8_OcD1BF"
      },
      "source": [
        "### Criando uma Series a partir de uma lista"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yEZR6DWiD1BF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a7d9c065-7b86-4e59-fe3e-7d9686298816"
      },
      "source": [
        "carros = [\"Jetta Variant\", \"Passat\", \"Crossfox\"]\n",
        "carros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Jetta Variant', 'Passat', 'Crossfox']"
            ]
          },
          "metadata": {},
          "execution_count": 257
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rLudWKZ_D1BF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "43c0b579-75da-44dd-f361-f9e2be90e117"
      },
      "source": [
        "pd.Series(carros)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    Jetta Variant\n",
              "1           Passat\n",
              "2         Crossfox\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 258
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VYVIKd1-D1BG"
      },
      "source": [
        "### Criando um DataFrame a partir de uma lista de dicionários"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QFNS9PckD1BG"
      },
      "source": [
        "dados = [\n",
        "    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},\n",
        "    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},\n",
        "    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}\n",
        "]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WDQb9AnKD1BH"
      },
      "source": [
        "dataset = pd.DataFrame(dados)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-2-jGvmGD1BI",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "cbadec33-b446-4399-b209-630281241ded"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            Nome            Motor   Ano  Quilometragem  Zero_km      Valor\n",
              "0  Jetta Variant  Motor 4.0 Turbo  2003        44410.0    False   88078.64\n",
              "1         Passat     Motor Diesel  1991         5712.0    False  106161.94\n",
              "2       Crossfox  Motor Diesel V8  1990        37123.0    False   72832.16"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f49c9970-d212-4ba8-b8be-213216995a00\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f49c9970-d212-4ba8-b8be-213216995a00')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-f49c9970-d212-4ba8-b8be-213216995a00 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-f49c9970-d212-4ba8-b8be-213216995a00');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 261
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2kbyOThiD1BJ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "7ec97791-2435-465d-e286-33c284db2f14"
      },
      "source": [
        "dataset[['Nome', 'Motor', 'Quilometragem', 'Zero_km', 'Ano', 'Valor']] #trocar ordem das colunas só nesse ponto"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            Nome            Motor  Quilometragem  Zero_km   Ano      Valor\n",
              "0  Jetta Variant  Motor 4.0 Turbo        44410.0    False  2003   88078.64\n",
              "1         Passat     Motor Diesel         5712.0    False  1991  106161.94\n",
              "2       Crossfox  Motor Diesel V8        37123.0    False  1990   72832.16"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-339c3399-7fa9-449b-884b-a1157fb4a849\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>2003</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>1991</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>1990</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-339c3399-7fa9-449b-884b-a1157fb4a849')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-339c3399-7fa9-449b-884b-a1157fb4a849 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-339c3399-7fa9-449b-884b-a1157fb4a849');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 262
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pJK2tQgYD1BK"
      },
      "source": [
        "### Criando um DataFrame a partir de um dicionário"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WKNQwKucD1BK"
      },
      "source": [
        "dados = {\n",
        "    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], \n",
        "    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],\n",
        "    'Ano': [2003, 1991, 1990],\n",
        "    'Quilometragem': [44410.0, 5712.0, 37123.0],\n",
        "    'Zero_km': [False, False, False],\n",
        "    'Valor': [88078.64, 106161.94, 72832.16]\n",
        "}"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lKnuZfzcD1BK"
      },
      "source": [
        "dataset = pd.DataFrame(dados)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PNqTytC-D1BL",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "8943209a-2508-4384-9073-ee66dc66e717"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            Nome            Motor   Ano  Quilometragem  Zero_km      Valor\n",
              "0  Jetta Variant  Motor 4.0 Turbo  2003        44410.0    False   88078.64\n",
              "1         Passat     Motor Diesel  1991         5712.0    False  106161.94\n",
              "2       Crossfox  Motor Diesel V8  1990        37123.0    False   72832.16"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ca4a47c3-c1f4-48fe-84ed-66fda964ce30\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ca4a47c3-c1f4-48fe-84ed-66fda964ce30')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ca4a47c3-c1f4-48fe-84ed-66fda964ce30 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ca4a47c3-c1f4-48fe-84ed-66fda964ce30');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 265
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fCCXs0reD1BL"
      },
      "source": [
        "### Criando um DataFrame a partir de uma arquivo externo"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "78PRHGeZD1BL"
      },
      "source": [
        "dataset = pd.read_csv('db.csv', sep = ';', index_col = 0) #index col torna a coluna indicada a principal"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "1o1YlnVPD1BM",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "outputId": "a2908cb5-f9c1-4d2d-881c-20fd8d5bdae2"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                       Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                                         \n",
              "Jetta Variant                Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat                          Motor Diesel  1991         5712.0    False   \n",
              "Crossfox                     Motor Diesel V8  1990        37123.0    False   \n",
              "DS5                          Motor 2.4 Turbo  2019            NaN     True   \n",
              "Aston Martin DB4             Motor 2.4 Turbo  2006        25757.0    False   \n",
              "...                                      ...   ...            ...      ...   \n",
              "Phantom 2013                        Motor V8  2014        27505.0    False   \n",
              "Cadillac Ciel concept               Motor V8  1991        29981.0    False   \n",
              "Classe GLK             Motor 5.0 V8 Bi-Turbo  2002        52637.0    False   \n",
              "Aston Martin DB5                Motor Diesel  1996         7685.0    False   \n",
              "Macan                        Motor Diesel V6  1992        50188.0    False   \n",
              "\n",
              "                                                              Acessórios  \\\n",
              "Nome                                                                       \n",
              "Jetta Variant          ['Rodas de liga', 'Travas elétricas', 'Piloto ...   \n",
              "Passat                 ['Central multimídia', 'Teto panorâmico', 'Fre...   \n",
              "Crossfox               ['Piloto automático', 'Controle de estabilidad...   \n",
              "DS5                    ['Travas elétricas', '4 X 4', 'Vidros elétrico...   \n",
              "Aston Martin DB4       ['Rodas de liga', '4 X 4', 'Central multimídia...   \n",
              "...                                                                  ...   \n",
              "Phantom 2013           ['Controle de estabilidade', 'Piloto automátic...   \n",
              "Cadillac Ciel concept  ['Bancos de couro', 'Painel digital', 'Sensor ...   \n",
              "Classe GLK             ['Rodas de liga', 'Controle de tração', 'Câmbi...   \n",
              "Aston Martin DB5       ['Ar condicionado', '4 X 4', 'Câmbio automátic...   \n",
              "Macan                  ['Central multimídia', 'Teto panorâmico', 'Vid...   \n",
              "\n",
              "                           Valor  \n",
              "Nome                              \n",
              "Jetta Variant           88078.64  \n",
              "Passat                 106161.94  \n",
              "Crossfox                72832.16  \n",
              "DS5                    124549.07  \n",
              "Aston Martin DB4        92612.10  \n",
              "...                          ...  \n",
              "Phantom 2013            51759.58  \n",
              "Cadillac Ciel concept   51667.06  \n",
              "Classe GLK              68934.03  \n",
              "Aston Martin DB5       122110.90  \n",
              "Macan                   90381.47  \n",
              "\n",
              "[258 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-330b254a-395c-47f5-bf3d-9c7384d45af4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Phantom 2013</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2014</td>\n",
              "      <td>27505.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Piloto automátic...</td>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cadillac Ciel concept</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>1991</td>\n",
              "      <td>29981.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Painel digital', 'Sensor ...</td>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Classe GLK</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2002</td>\n",
              "      <td>52637.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Controle de tração', 'Câmbi...</td>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Macan</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>1992</td>\n",
              "      <td>50188.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Vid...</td>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 6 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-330b254a-395c-47f5-bf3d-9c7384d45af4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-330b254a-395c-47f5-bf3d-9c7384d45af4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-330b254a-395c-47f5-bf3d-9c7384d45af4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 360
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y5V-1AK-D1BN"
      },
      "source": [
        "# 5.2 Seleções com DataFrames"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wZjqlHe9D1BN"
      },
      "source": [
        "### Selecionando colunas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "gM3LbtzlD1BN",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 579
        },
        "outputId": "bf3b5dc8-7abf-490e-b619-dfcc5e9747f7"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                            Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                              \n",
              "Jetta Variant     Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat               Motor Diesel  1991         5712.0    False   \n",
              "Crossfox          Motor Diesel V8  1990        37123.0    False   \n",
              "DS5               Motor 2.4 Turbo  2019            NaN     True   \n",
              "Aston Martin DB4  Motor 2.4 Turbo  2006        25757.0    False   \n",
              "\n",
              "                                                         Acessórios      Valor  \n",
              "Nome                                                                            \n",
              "Jetta Variant     ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "Passat            ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "Crossfox          ['Piloto automático', 'Controle de estabilidad...   72832.16  \n",
              "DS5               ['Travas elétricas', '4 X 4', 'Vidros elétrico...  124549.07  \n",
              "Aston Martin DB4  ['Rodas de liga', '4 X 4', 'Central multimídia...   92612.10  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bc436491-f3d2-41e3-88dd-06b984201820\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bc436491-f3d2-41e3-88dd-06b984201820')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bc436491-f3d2-41e3-88dd-06b984201820 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bc436491-f3d2-41e3-88dd-06b984201820');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 268
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R2FWgCM_D1BO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "39a5ea7d-ac07-4d0a-c369-de1c3e04d2fd"
      },
      "source": [
        "dataset['Valor']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Nome\n",
              "Jetta Variant             88078.64\n",
              "Passat                   106161.94\n",
              "Crossfox                  72832.16\n",
              "DS5                      124549.07\n",
              "Aston Martin DB4          92612.10\n",
              "                           ...    \n",
              "Phantom 2013              51759.58\n",
              "Cadillac Ciel concept     51667.06\n",
              "Classe GLK                68934.03\n",
              "Aston Martin DB5         122110.90\n",
              "Macan                     90381.47\n",
              "Name: Valor, Length: 258, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 269
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "lCCumsxsD1BP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ac4d1370-ef87-41a5-8848-3e98dd596bcd"
      },
      "source": [
        "type(dataset['Valor'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.series.Series"
            ]
          },
          "metadata": {},
          "execution_count": 270
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zxlyC3B8D1BP",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 675
        },
        "outputId": "ea4fddad-1904-4aa4-c5c6-3bd7246a0f9c"
      },
      "source": [
        "dataset[['Valor']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                           Valor\n",
              "Nome                            \n",
              "Jetta Variant           88078.64\n",
              "Passat                 106161.94\n",
              "Crossfox                72832.16\n",
              "DS5                    124549.07\n",
              "Aston Martin DB4        92612.10\n",
              "...                          ...\n",
              "Phantom 2013            51759.58\n",
              "Cadillac Ciel concept   51667.06\n",
              "Classe GLK              68934.03\n",
              "Aston Martin DB5       122110.90\n",
              "Macan                   90381.47\n",
              "\n",
              "[258 rows x 1 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-eeaf8813-8d4e-4be1-8c5b-d558c3f87a5f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Phantom 2013</th>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cadillac Ciel concept</th>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Classe GLK</th>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Macan</th>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 1 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-eeaf8813-8d4e-4be1-8c5b-d558c3f87a5f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-eeaf8813-8d4e-4be1-8c5b-d558c3f87a5f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-eeaf8813-8d4e-4be1-8c5b-d558c3f87a5f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 271
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(dataset[['Valor']])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b2C1zhDOC6Uf",
        "outputId": "0392b395-d82e-4852-cd95-f751d13f6fc9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {},
          "execution_count": 272
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7RPXPm1XD1BQ"
      },
      "source": [
        "### Selecionando linhas - [ i : j ] \n",
        "\n",
        "<font color=red>**Observação:**</font> A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é **incluída** e a linha com índice j **não é incluída** no resultado."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PdDUwPw3D1BQ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 412
        },
        "outputId": "1314c9bd-de69-4237-f219-2fd8cdf9d635"
      },
      "source": [
        "dataset[0:3]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                         Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                           \n",
              "Jetta Variant  Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat            Motor Diesel  1991         5712.0    False   \n",
              "Crossfox       Motor Diesel V8  1990        37123.0    False   \n",
              "\n",
              "                                                      Acessórios      Valor  \n",
              "Nome                                                                         \n",
              "Jetta Variant  ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "Passat         ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "Crossfox       ['Piloto automático', 'Controle de estabilidad...   72832.16  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-713b762c-49d7-4d06-aab6-5f575147b7c5\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-713b762c-49d7-4d06-aab6-5f575147b7c5')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-713b762c-49d7-4d06-aab6-5f575147b7c5 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-713b762c-49d7-4d06-aab6-5f575147b7c5');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 273
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G3DMSk97D1BR"
      },
      "source": [
        "### Utilizando .loc para seleções\n",
        "\n",
        "<font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "oOEO72uZD1BT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3456a123-1358-4880-f422-58fd17d17dbb"
      },
      "source": [
        "dataset.loc['Passat']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Motor                                                 Motor Diesel\n",
              "Ano                                                           1991\n",
              "Quilometragem                                               5712.0\n",
              "Zero_km                                                      False\n",
              "Acessórios       ['Central multimídia', 'Teto panorâmico', 'Fre...\n",
              "Valor                                                    106161.94\n",
              "Name: Passat, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 274
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ftg-hNOoD1BR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 329
        },
        "outputId": "4dc10d34-01c6-4642-e8b0-d032505087bd"
      },
      "source": [
        "dataset.loc[['Passat', 'DS5']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                    \n",
              "Passat     Motor Diesel  1991         5712.0    False   \n",
              "DS5     Motor 2.4 Turbo  2019            NaN     True   \n",
              "\n",
              "                                               Acessórios      Valor  \n",
              "Nome                                                                  \n",
              "Passat  ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "DS5     ['Travas elétricas', '4 X 4', 'Vidros elétrico...  124549.07  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ec7ffc76-96d1-4fb0-91f9-51c261febe10\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ec7ffc76-96d1-4fb0-91f9-51c261febe10')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ec7ffc76-96d1-4fb0-91f9-51c261febe10 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ec7ffc76-96d1-4fb0-91f9-51c261febe10');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 275
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xdxkDrHvD1BS",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 259
        },
        "outputId": "a8c8a5de-620f-4892-b796-16755e0f3e2f"
      },
      "source": [
        "dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  Motor      Valor\n",
              "Nome                              \n",
              "Passat     Motor Diesel  106161.94\n",
              "DS5     Motor 2.4 Turbo  124549.07"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-88c2cce8-74b2-4c9e-b9ef-7bc123618a3d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-88c2cce8-74b2-4c9e-b9ef-7bc123618a3d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-88c2cce8-74b2-4c9e-b9ef-7bc123618a3d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-88c2cce8-74b2-4c9e-b9ef-7bc123618a3d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 276
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pMN3U1KjD1BS",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 849
        },
        "outputId": "51ee1301-ded4-4096-e5a9-410589e89c11"
      },
      "source": [
        "dataset.loc[:, ['Motor', 'Valor']]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                       Motor      Valor\n",
              "Nome                                                   \n",
              "Jetta Variant                Motor 4.0 Turbo   88078.64\n",
              "Passat                          Motor Diesel  106161.94\n",
              "Crossfox                     Motor Diesel V8   72832.16\n",
              "DS5                          Motor 2.4 Turbo  124549.07\n",
              "Aston Martin DB4             Motor 2.4 Turbo   92612.10\n",
              "...                                      ...        ...\n",
              "Phantom 2013                        Motor V8   51759.58\n",
              "Cadillac Ciel concept               Motor V8   51667.06\n",
              "Classe GLK             Motor 5.0 V8 Bi-Turbo   68934.03\n",
              "Aston Martin DB5                Motor Diesel  122110.90\n",
              "Macan                        Motor Diesel V6   90381.47\n",
              "\n",
              "[258 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3427c733-e099-4868-b272-b1a3110d8237\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Phantom 2013</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cadillac Ciel concept</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Classe GLK</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Macan</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3427c733-e099-4868-b272-b1a3110d8237')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3427c733-e099-4868-b272-b1a3110d8237 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3427c733-e099-4868-b272-b1a3110d8237');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 277
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(dataset[['Valor']])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sdzMu9f_pRAj",
        "outputId": "2391c234-4a41-4bb4-e267-3f59da8c59b1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {},
          "execution_count": 278
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SYKEe3vCD1BT"
      },
      "source": [
        "### Utilizando .iloc para seleções\n",
        "\n",
        "<font color=red>**Observação:**</font> Seleciona com base nos índices, ou seja, se baseia na posição das informações."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U4Bru90bD1BT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4de01637-364c-4221-bc3e-f717d8168f22"
      },
      "source": [
        "dataset.iloc[1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Motor                                                 Motor Diesel\n",
              "Ano                                                           1991\n",
              "Quilometragem                                               5712.0\n",
              "Zero_km                                                      False\n",
              "Acessórios       ['Central multimídia', 'Teto panorâmico', 'Fre...\n",
              "Valor                                                    106161.94\n",
              "Name: Passat, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 279
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iLKUyrzND1BU",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "outputId": "d594fc2b-98e4-4b0f-f88a-f392704162f0"
      },
      "source": [
        "dataset.iloc[[1]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                 \n",
              "Passat  Motor Diesel  1991         5712.0    False   \n",
              "\n",
              "                                               Acessórios      Valor  \n",
              "Nome                                                                  \n",
              "Passat  ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b230ff8c-d5f9-40dc-9d34-8fc8a5a47579\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b230ff8c-d5f9-40dc-9d34-8fc8a5a47579')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b230ff8c-d5f9-40dc-9d34-8fc8a5a47579 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b230ff8c-d5f9-40dc-9d34-8fc8a5a47579');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 280
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KGZpixYUD1BU",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "outputId": "4574fe34-9441-422d-ba43-898d4f15da82"
      },
      "source": [
        "dataset.iloc[53:59]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                                  Motor   Ano  Quilometragem  \\\n",
              "Nome                                                                           \n",
              "Aston Martin V8 Vantage Roadster        Motor 2.4 Turbo  2006        93947.0   \n",
              "Hoggar                            Motor 5.0 V8 Bi-Turbo  2010        35345.0   \n",
              "A1                                Motor 5.0 V8 Bi-Turbo  1994        81007.0   \n",
              "Aston Martin DB7 Vantage                       Motor V6  2007       119513.0   \n",
              "CLA                                        Motor 1.0 8v  2019            NaN   \n",
              "Accord                                         Motor V8  2019            NaN   \n",
              "\n",
              "                                  Zero_km  \\\n",
              "Nome                                        \n",
              "Aston Martin V8 Vantage Roadster    False   \n",
              "Hoggar                              False   \n",
              "A1                                  False   \n",
              "Aston Martin DB7 Vantage            False   \n",
              "CLA                                  True   \n",
              "Accord                               True   \n",
              "\n",
              "                                                                         Acessórios  \\\n",
              "Nome                                                                                  \n",
              "Aston Martin V8 Vantage Roadster  ['Câmbio automático', 'Câmera de estacionament...   \n",
              "Hoggar                            ['Controle de estabilidade', 'Bancos de couro'...   \n",
              "A1                                ['Painel digital', 'Câmbio automático', 'Câmer...   \n",
              "Aston Martin DB7 Vantage          ['Sensor crepuscular', 'Piloto automático', 'T...   \n",
              "CLA                               ['Central multimídia', 'Sensor de chuva', 'Con...   \n",
              "Accord                            ['Sensor de estacionamento', 'Ar condicionado'...   \n",
              "\n",
              "                                      Valor  \n",
              "Nome                                         \n",
              "Aston Martin V8 Vantage Roadster   80422.71  \n",
              "Hoggar                             56373.99  \n",
              "A1                                 70846.03  \n",
              "Aston Martin DB7 Vantage          128694.23  \n",
              "CLA                               133329.19  \n",
              "Accord                            131961.43  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-469a14fe-f5f0-47a2-946c-689daf043459\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Aston Martin V8 Vantage Roadster</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>93947.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Câmbio automático', 'Câmera de estacionament...</td>\n",
              "      <td>80422.71</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Hoggar</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2010</td>\n",
              "      <td>35345.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Bancos de couro'...</td>\n",
              "      <td>56373.99</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A1</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>1994</td>\n",
              "      <td>81007.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Painel digital', 'Câmbio automático', 'Câmer...</td>\n",
              "      <td>70846.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB7 Vantage</th>\n",
              "      <td>Motor V6</td>\n",
              "      <td>2007</td>\n",
              "      <td>119513.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Sensor crepuscular', 'Piloto automático', 'T...</td>\n",
              "      <td>128694.23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CLA</th>\n",
              "      <td>Motor 1.0 8v</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Central multimídia', 'Sensor de chuva', 'Con...</td>\n",
              "      <td>133329.19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Accord</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor de estacionamento', 'Ar condicionado'...</td>\n",
              "      <td>131961.43</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-469a14fe-f5f0-47a2-946c-689daf043459')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-469a14fe-f5f0-47a2-946c-689daf043459 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-469a14fe-f5f0-47a2-946c-689daf043459');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 281
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GxdqIz4LD1BV",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "outputId": "4ca321ab-ba98-4d41-f3c0-1ab7f63aa940"
      },
      "source": [
        "dataset.iloc[1:4, [0, 5, 2]] #seleciona um conjunto de linhas"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    Motor      Valor  Quilometragem\n",
              "Nome                                               \n",
              "Passat       Motor Diesel  106161.94         5712.0\n",
              "Crossfox  Motor Diesel V8   72832.16        37123.0\n",
              "DS5       Motor 2.4 Turbo  124549.07            NaN"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c0e66617-5b4c-4db0-848a-a9e33b3aea31\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Valor</th>\n",
              "      <th>Quilometragem</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>106161.94</td>\n",
              "      <td>5712.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>72832.16</td>\n",
              "      <td>37123.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>124549.07</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c0e66617-5b4c-4db0-848a-a9e33b3aea31')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c0e66617-5b4c-4db0-848a-a9e33b3aea31 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c0e66617-5b4c-4db0-848a-a9e33b3aea31');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 282
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.iloc[[1, 42, 22, 53], [0, 5, 2]] #pode selecionar colunas e linhas especificas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "lRPNYBFZqpE4",
        "outputId": "39b4c439-5e72-4e0c-b1c0-ac9a11c8e285"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                            Motor      Valor  Quilometragem\n",
              "Nome                                                                       \n",
              "Passat                               Motor Diesel  106161.94         5712.0\n",
              "Optima                              Motor 1.8 16v   86641.34            NaN\n",
              "Lamborghini Obvious               Motor Diesel V6  133529.84        98079.0\n",
              "Aston Martin V8 Vantage Roadster  Motor 2.4 Turbo   80422.71        93947.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c1dd84ef-3030-487f-8e02-0474b79387b3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Valor</th>\n",
              "      <th>Quilometragem</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>106161.94</td>\n",
              "      <td>5712.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Optima</th>\n",
              "      <td>Motor 1.8 16v</td>\n",
              "      <td>86641.34</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Lamborghini Obvious</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>133529.84</td>\n",
              "      <td>98079.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin V8 Vantage Roadster</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>80422.71</td>\n",
              "      <td>93947.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c1dd84ef-3030-487f-8e02-0474b79387b3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c1dd84ef-3030-487f-8e02-0474b79387b3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c1dd84ef-3030-487f-8e02-0474b79387b3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 283
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.iloc[:, [0, 5, 2]] # usa 2 pontos pra selecionar todos"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "uIN9WuUcq7Fo",
        "outputId": "6ad90ae1-356f-40f1-9291-6b7a5e0f158d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                       Motor      Valor  Quilometragem\n",
              "Nome                                                                  \n",
              "Jetta Variant                Motor 4.0 Turbo   88078.64        44410.0\n",
              "Passat                          Motor Diesel  106161.94         5712.0\n",
              "Crossfox                     Motor Diesel V8   72832.16        37123.0\n",
              "DS5                          Motor 2.4 Turbo  124549.07            NaN\n",
              "Aston Martin DB4             Motor 2.4 Turbo   92612.10        25757.0\n",
              "...                                      ...        ...            ...\n",
              "Phantom 2013                        Motor V8   51759.58        27505.0\n",
              "Cadillac Ciel concept               Motor V8   51667.06        29981.0\n",
              "Classe GLK             Motor 5.0 V8 Bi-Turbo   68934.03        52637.0\n",
              "Aston Martin DB5                Motor Diesel  122110.90         7685.0\n",
              "Macan                        Motor Diesel V6   90381.47        50188.0\n",
              "\n",
              "[258 rows x 3 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d73e136c-78a1-4239-a377-cd84eef04e31\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Valor</th>\n",
              "      <th>Quilometragem</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>88078.64</td>\n",
              "      <td>44410.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>106161.94</td>\n",
              "      <td>5712.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>72832.16</td>\n",
              "      <td>37123.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>124549.07</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>92612.10</td>\n",
              "      <td>25757.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Phantom 2013</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>51759.58</td>\n",
              "      <td>27505.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cadillac Ciel concept</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>51667.06</td>\n",
              "      <td>29981.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Classe GLK</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>68934.03</td>\n",
              "      <td>52637.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>122110.90</td>\n",
              "      <td>7685.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Macan</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>90381.47</td>\n",
              "      <td>50188.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 3 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d73e136c-78a1-4239-a377-cd84eef04e31')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d73e136c-78a1-4239-a377-cd84eef04e31 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d73e136c-78a1-4239-a377-cd84eef04e31');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 284
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eAbwq1oLD1BW"
      },
      "source": [
        "# 5.3 Queries com DataFrames"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "AOZTWzehD1BW",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "outputId": "5ffe6783-e52b-4843-e341-8e47cc092857"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                            Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                              \n",
              "Jetta Variant     Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat               Motor Diesel  1991         5712.0    False   \n",
              "Crossfox          Motor Diesel V8  1990        37123.0    False   \n",
              "DS5               Motor 2.4 Turbo  2019            NaN     True   \n",
              "Aston Martin DB4  Motor 2.4 Turbo  2006        25757.0    False   \n",
              "\n",
              "                                                         Acessórios      Valor  \n",
              "Nome                                                                            \n",
              "Jetta Variant     ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "Passat            ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "Crossfox          ['Piloto automático', 'Controle de estabilidad...   72832.16  \n",
              "DS5               ['Travas elétricas', '4 X 4', 'Vidros elétrico...  124549.07  \n",
              "Aston Martin DB4  ['Rodas de liga', '4 X 4', 'Central multimídia...   92612.10  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ba9ba785-d2f1-4aba-8aaf-ad17cddee1e9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ba9ba785-d2f1-4aba-8aaf-ad17cddee1e9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ba9ba785-d2f1-4aba-8aaf-ad17cddee1e9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ba9ba785-d2f1-4aba-8aaf-ad17cddee1e9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 285
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "rO5T4h94D1BX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2eec3b24-c214-48cc-ab51-3d23f47dd103"
      },
      "source": [
        "dataset.Motor"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Nome\n",
              "Jetta Variant                  Motor 4.0 Turbo\n",
              "Passat                            Motor Diesel\n",
              "Crossfox                       Motor Diesel V8\n",
              "DS5                            Motor 2.4 Turbo\n",
              "Aston Martin DB4               Motor 2.4 Turbo\n",
              "                                 ...          \n",
              "Phantom 2013                          Motor V8\n",
              "Cadillac Ciel concept                 Motor V8\n",
              "Classe GLK               Motor 5.0 V8 Bi-Turbo\n",
              "Aston Martin DB5                  Motor Diesel\n",
              "Macan                          Motor Diesel V6\n",
              "Name: Motor, Length: 258, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 286
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "STZ-l8oaD1BX"
      },
      "source": [
        "select = dataset.Motor == \"Motor Diesel\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(select)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bNFUEfhIm_VX",
        "outputId": "0100eedc-451b-4850-bcf4-00626d761c82"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.series.Series"
            ]
          },
          "metadata": {},
          "execution_count": 288
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset[select]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "jk3FVVgxm_Js",
        "outputId": "4daff17f-370a-4391-df17-35e6bbd28a49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                              Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                                \n",
              "Passat                 Motor Diesel  1991         5712.0    False   \n",
              "Effa Hafei Picape Baú  Motor Diesel  1991       102959.0    False   \n",
              "Sorento                Motor Diesel  2019            NaN     True   \n",
              "New Fiesta Hatch       Motor Diesel  2017       118895.0    False   \n",
              "Kangoo Express         Motor Diesel  2007        29132.0    False   \n",
              "...                             ...   ...            ...      ...   \n",
              "Dodge Dakota           Motor Diesel  1993        71544.0    False   \n",
              "i30 CW                 Motor Diesel  2015         8497.0    False   \n",
              "Série 7 Sedã           Motor Diesel  2019            NaN     True   \n",
              "V60                    Motor Diesel  2004        91840.0    False   \n",
              "Aston Martin DB5       Motor Diesel  1996         7685.0    False   \n",
              "\n",
              "                                                              Acessórios  \\\n",
              "Nome                                                                       \n",
              "Passat                 ['Central multimídia', 'Teto panorâmico', 'Fre...   \n",
              "Effa Hafei Picape Baú  ['Controle de estabilidade', 'Painel digital',...   \n",
              "Sorento                ['Sensor de chuva', 'Câmera de estacionamento'...   \n",
              "New Fiesta Hatch       ['Sensor de estacionamento', 'Travas elétricas...   \n",
              "Kangoo Express         ['Bancos de couro', 'Câmbio automático', 'Pilo...   \n",
              "...                                                                  ...   \n",
              "Dodge Dakota           ['Controle de tração', 'Sensor de estacionamen...   \n",
              "i30 CW                 ['Sensor de chuva', 'Vidros elétricos', 'Contr...   \n",
              "Série 7 Sedã           ['Vidros elétricos', 'Travas elétricas', 'Roda...   \n",
              "V60                    ['Rodas de liga', 'Sensor crepuscular', 'Ar co...   \n",
              "Aston Martin DB5       ['Ar condicionado', '4 X 4', 'Câmbio automátic...   \n",
              "\n",
              "                           Valor  \n",
              "Nome                              \n",
              "Passat                 106161.94  \n",
              "Effa Hafei Picape Baú  125684.65  \n",
              "Sorento                 81399.35  \n",
              "New Fiesta Hatch        66007.16  \n",
              "Kangoo Express         146716.91  \n",
              "...                          ...  \n",
              "Dodge Dakota           141083.35  \n",
              "i30 CW                  73311.75  \n",
              "Série 7 Sedã            67539.79  \n",
              "V60                    114728.74  \n",
              "Aston Martin DB5       122110.90  \n",
              "\n",
              "[26 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-93227bf4-64e6-4a75-bcb9-1a996d7219b9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Effa Hafei Picape Baú</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>102959.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Painel digital',...</td>\n",
              "      <td>125684.65</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Sorento</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor de chuva', 'Câmera de estacionamento'...</td>\n",
              "      <td>81399.35</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>New Fiesta Hatch</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2017</td>\n",
              "      <td>118895.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Sensor de estacionamento', 'Travas elétricas...</td>\n",
              "      <td>66007.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Kangoo Express</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2007</td>\n",
              "      <td>29132.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Câmbio automático', 'Pilo...</td>\n",
              "      <td>146716.91</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Dodge Dakota</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1993</td>\n",
              "      <td>71544.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de tração', 'Sensor de estacionamen...</td>\n",
              "      <td>141083.35</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>i30 CW</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2015</td>\n",
              "      <td>8497.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Sensor de chuva', 'Vidros elétricos', 'Contr...</td>\n",
              "      <td>73311.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Série 7 Sedã</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Vidros elétricos', 'Travas elétricas', 'Roda...</td>\n",
              "      <td>67539.79</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>V60</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2004</td>\n",
              "      <td>91840.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Sensor crepuscular', 'Ar co...</td>\n",
              "      <td>114728.74</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>26 rows × 6 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-93227bf4-64e6-4a75-bcb9-1a996d7219b9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-93227bf4-64e6-4a75-bcb9-1a996d7219b9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-93227bf4-64e6-4a75-bcb9-1a996d7219b9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 289
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset[(dataset.Motor == \"Motor Diesel\") & (dataset.Zero_km == True)]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "id": "b3LqFhLcmWst",
        "outputId": "4df5005c-7852-441b-83ed-3fcf48e52b90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                            Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                              \n",
              "Sorento              Motor Diesel  2019            NaN     True   \n",
              "Cielo Hatch          Motor Diesel  2019            NaN     True   \n",
              "Camry                Motor Diesel  2019            NaN     True   \n",
              "Aston Martin Virage  Motor Diesel  2019            NaN     True   \n",
              "Série 7 Sedã         Motor Diesel  2019            NaN     True   \n",
              "\n",
              "                                                            Acessórios  \\\n",
              "Nome                                                                     \n",
              "Sorento              ['Sensor de chuva', 'Câmera de estacionamento'...   \n",
              "Cielo Hatch          ['Painel digital', 'Central multimídia', 'Câme...   \n",
              "Camry                ['Travas elétricas', 'Rodas de liga', 'Sensor ...   \n",
              "Aston Martin Virage  ['Travas elétricas', 'Controle de tração', 'Câ...   \n",
              "Série 7 Sedã         ['Vidros elétricos', 'Travas elétricas', 'Roda...   \n",
              "\n",
              "                         Valor  \n",
              "Nome                            \n",
              "Sorento               81399.35  \n",
              "Cielo Hatch          145197.70  \n",
              "Camry                138597.27  \n",
              "Aston Martin Virage   97290.18  \n",
              "Série 7 Sedã          67539.79  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b667e633-7ac8-4f18-9045-d730e8a921ff\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Sorento</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor de chuva', 'Câmera de estacionamento'...</td>\n",
              "      <td>81399.35</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cielo Hatch</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Painel digital', 'Central multimídia', 'Câme...</td>\n",
              "      <td>145197.70</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Camry</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Rodas de liga', 'Sensor ...</td>\n",
              "      <td>138597.27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin Virage</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Controle de tração', 'Câ...</td>\n",
              "      <td>97290.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Série 7 Sedã</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Vidros elétricos', 'Travas elétricas', 'Roda...</td>\n",
              "      <td>67539.79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b667e633-7ac8-4f18-9045-d730e8a921ff')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b667e633-7ac8-4f18-9045-d730e8a921ff button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b667e633-7ac8-4f18-9045-d730e8a921ff');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 290
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OZC8NAn6D1BX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "010a9174-6fc6-4392-9f4a-7d07ed52ed35"
      },
      "source": [
        "(dataset.Motor == \"Motor Diesel\") & (dataset.Zero_km == True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Nome\n",
              "Jetta Variant            False\n",
              "Passat                   False\n",
              "Crossfox                 False\n",
              "DS5                      False\n",
              "Aston Martin DB4         False\n",
              "                         ...  \n",
              "Phantom 2013             False\n",
              "Cadillac Ciel concept    False\n",
              "Classe GLK               False\n",
              "Aston Martin DB5         False\n",
              "Macan                    False\n",
              "Length: 258, dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 291
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_XKXcWO-D1BY"
      },
      "source": [
        "### Utilizando o método query"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AB9JirSoD1BY",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "outputId": "9c2267ce-5448-4319-e918-6f14a6c22e26"
      },
      "source": [
        "dataset.query('Motor == \"Motor Diesel\" and Zero_km == True') #Pra escolher colunas com espaço no nome"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                            Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                              \n",
              "Sorento              Motor Diesel  2019            NaN     True   \n",
              "Cielo Hatch          Motor Diesel  2019            NaN     True   \n",
              "Camry                Motor Diesel  2019            NaN     True   \n",
              "Aston Martin Virage  Motor Diesel  2019            NaN     True   \n",
              "Série 7 Sedã         Motor Diesel  2019            NaN     True   \n",
              "\n",
              "                                                            Acessórios  \\\n",
              "Nome                                                                     \n",
              "Sorento              ['Sensor de chuva', 'Câmera de estacionamento'...   \n",
              "Cielo Hatch          ['Painel digital', 'Central multimídia', 'Câme...   \n",
              "Camry                ['Travas elétricas', 'Rodas de liga', 'Sensor ...   \n",
              "Aston Martin Virage  ['Travas elétricas', 'Controle de tração', 'Câ...   \n",
              "Série 7 Sedã         ['Vidros elétricos', 'Travas elétricas', 'Roda...   \n",
              "\n",
              "                         Valor  \n",
              "Nome                            \n",
              "Sorento               81399.35  \n",
              "Cielo Hatch          145197.70  \n",
              "Camry                138597.27  \n",
              "Aston Martin Virage   97290.18  \n",
              "Série 7 Sedã          67539.79  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ff03f22f-e033-414b-9099-3d943a6ee10e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Sorento</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor de chuva', 'Câmera de estacionamento'...</td>\n",
              "      <td>81399.35</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cielo Hatch</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Painel digital', 'Central multimídia', 'Câme...</td>\n",
              "      <td>145197.70</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Camry</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Rodas de liga', 'Sensor ...</td>\n",
              "      <td>138597.27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin Virage</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Controle de tração', 'Câ...</td>\n",
              "      <td>97290.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Série 7 Sedã</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Vidros elétricos', 'Travas elétricas', 'Roda...</td>\n",
              "      <td>67539.79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ff03f22f-e033-414b-9099-3d943a6ee10e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ff03f22f-e033-414b-9099-3d943a6ee10e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ff03f22f-e033-414b-9099-3d943a6ee10e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 293
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ciJ4dw_FD1BZ"
      },
      "source": [
        "# 5.4 Iterando com DataFrames"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TKAB-g5KD1BZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ab5fab78-36db-4179-c419-f8054a2b18a3"
      },
      "source": [
        "for item in dataset:\n",
        "  print(item)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Motor\n",
            "Ano\n",
            "Quilometragem\n",
            "Zero_km\n",
            "Acessórios\n",
            "Valor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eFTNtPRWD1Ba"
      },
      "source": [
        "# list(dataset.iterrows()) cria uma lista com todas as tuplas"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for index, row in dataset.iterrows():\n",
        "  if(2019 - row['Ano'] != 0):\n",
        "    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])\n",
        "  else:\n",
        "    dataset.loc[index, 'Km_media'] = 0\n",
        "\n",
        "dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "3gAvCgfRq7KA",
        "outputId": "9bae9e5a-27e7-4539-e67c-2f973bab8724"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                       Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                                         \n",
              "Jetta Variant                Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat                          Motor Diesel  1991         5712.0    False   \n",
              "Crossfox                     Motor Diesel V8  1990        37123.0    False   \n",
              "DS5                          Motor 2.4 Turbo  2019            NaN     True   \n",
              "Aston Martin DB4             Motor 2.4 Turbo  2006        25757.0    False   \n",
              "...                                      ...   ...            ...      ...   \n",
              "Phantom 2013                        Motor V8  2014        27505.0    False   \n",
              "Cadillac Ciel concept               Motor V8  1991        29981.0    False   \n",
              "Classe GLK             Motor 5.0 V8 Bi-Turbo  2002        52637.0    False   \n",
              "Aston Martin DB5                Motor Diesel  1996         7685.0    False   \n",
              "Macan                        Motor Diesel V6  1992        50188.0    False   \n",
              "\n",
              "                                                              Acessórios  \\\n",
              "Nome                                                                       \n",
              "Jetta Variant          ['Rodas de liga', 'Travas elétricas', 'Piloto ...   \n",
              "Passat                 ['Central multimídia', 'Teto panorâmico', 'Fre...   \n",
              "Crossfox               ['Piloto automático', 'Controle de estabilidad...   \n",
              "DS5                    ['Travas elétricas', '4 X 4', 'Vidros elétrico...   \n",
              "Aston Martin DB4       ['Rodas de liga', '4 X 4', 'Central multimídia...   \n",
              "...                                                                  ...   \n",
              "Phantom 2013           ['Controle de estabilidade', 'Piloto automátic...   \n",
              "Cadillac Ciel concept  ['Bancos de couro', 'Painel digital', 'Sensor ...   \n",
              "Classe GLK             ['Rodas de liga', 'Controle de tração', 'Câmbi...   \n",
              "Aston Martin DB5       ['Ar condicionado', '4 X 4', 'Câmbio automátic...   \n",
              "Macan                  ['Central multimídia', 'Teto panorâmico', 'Vid...   \n",
              "\n",
              "                           Valor     Km_media  \n",
              "Nome                                           \n",
              "Jetta Variant           88078.64  2775.625000  \n",
              "Passat                 106161.94   204.000000  \n",
              "Crossfox                72832.16  1280.103448  \n",
              "DS5                    124549.07     0.000000  \n",
              "Aston Martin DB4        92612.10  1981.307692  \n",
              "...                          ...          ...  \n",
              "Phantom 2013            51759.58  5501.000000  \n",
              "Cadillac Ciel concept   51667.06  1070.750000  \n",
              "Classe GLK              68934.03  3096.294118  \n",
              "Aston Martin DB5       122110.90   334.130435  \n",
              "Macan                   90381.47  1858.814815  \n",
              "\n",
              "[258 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a9a0eb3e-e289-468f-aa51-64d38ecc984e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "      <th>Km_media</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "      <td>2775.625000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "      <td>204.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "      <td>1280.103448</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "      <td>1981.307692</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Phantom 2013</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2014</td>\n",
              "      <td>27505.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Piloto automátic...</td>\n",
              "      <td>51759.58</td>\n",
              "      <td>5501.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Cadillac Ciel concept</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>1991</td>\n",
              "      <td>29981.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Painel digital', 'Sensor ...</td>\n",
              "      <td>51667.06</td>\n",
              "      <td>1070.750000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Classe GLK</th>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2002</td>\n",
              "      <td>52637.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Controle de tração', 'Câmbi...</td>\n",
              "      <td>68934.03</td>\n",
              "      <td>3096.294118</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB5</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "      <td>334.130435</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Macan</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>1992</td>\n",
              "      <td>50188.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Vid...</td>\n",
              "      <td>90381.47</td>\n",
              "      <td>1858.814815</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 7 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a9a0eb3e-e289-468f-aa51-64d38ecc984e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a9a0eb3e-e289-468f-aa51-64d38ecc984e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a9a0eb3e-e289-468f-aa51-64d38ecc984e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 297
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HnUzHFQPD1Ba"
      },
      "source": [
        "# 5.5 Tratamento de dados"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FRxBWoBGD1Ba",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "outputId": "065e0180-9fd3-4254-fbc1-fe85c39d4255"
      },
      "source": [
        "dataset.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                            Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                              \n",
              "Jetta Variant     Motor 4.0 Turbo  2003        44410.0    False   \n",
              "Passat               Motor Diesel  1991         5712.0    False   \n",
              "Crossfox          Motor Diesel V8  1990        37123.0    False   \n",
              "DS5               Motor 2.4 Turbo  2019            NaN     True   \n",
              "Aston Martin DB4  Motor 2.4 Turbo  2006        25757.0    False   \n",
              "\n",
              "                                                         Acessórios  \\\n",
              "Nome                                                                  \n",
              "Jetta Variant     ['Rodas de liga', 'Travas elétricas', 'Piloto ...   \n",
              "Passat            ['Central multimídia', 'Teto panorâmico', 'Fre...   \n",
              "Crossfox          ['Piloto automático', 'Controle de estabilidad...   \n",
              "DS5               ['Travas elétricas', '4 X 4', 'Vidros elétrico...   \n",
              "Aston Martin DB4  ['Rodas de liga', '4 X 4', 'Central multimídia...   \n",
              "\n",
              "                      Valor     Km_media  \n",
              "Nome                                      \n",
              "Jetta Variant      88078.64  2775.625000  \n",
              "Passat            106161.94   204.000000  \n",
              "Crossfox           72832.16  1280.103448  \n",
              "DS5               124549.07     0.000000  \n",
              "Aston Martin DB4   92612.10  1981.307692  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0cb7ccab-a20b-469d-913a-5e9befdc6a5f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "      <th>Km_media</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Jetta Variant</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "      <td>2775.625000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Passat</th>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "      <td>204.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Crossfox</th>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "      <td>1280.103448</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aston Martin DB4</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "      <td>1981.307692</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0cb7ccab-a20b-469d-913a-5e9befdc6a5f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-0cb7ccab-a20b-469d-913a-5e9befdc6a5f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-0cb7ccab-a20b-469d-913a-5e9befdc6a5f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 298
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HHSwH0ZaD1Bc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ccdd236-5c9d-4e34-b647-a1a00cf15e82"
      },
      "source": [
        "dataset.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Index: 258 entries, Jetta Variant to Macan\n",
            "Data columns (total 6 columns):\n",
            " #   Column         Non-Null Count  Dtype  \n",
            "---  ------         --------------  -----  \n",
            " 0   Motor          258 non-null    object \n",
            " 1   Ano            258 non-null    int64  \n",
            " 2   Quilometragem  197 non-null    float64\n",
            " 3   Zero_km        258 non-null    bool   \n",
            " 4   Acessórios     258 non-null    object \n",
            " 5   Valor          258 non-null    float64\n",
            "dtypes: bool(1), float64(2), int64(1), object(2)\n",
            "memory usage: 12.3+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "G27pxgZ5D1Bd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "outputId": "946380dd-119e-4e7b-c7d7-2b3ff6bf7c9b"
      },
      "source": [
        "dataset[dataset.Quilometragem.isna()]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                                  \n",
              "DS5                   Motor 2.4 Turbo  2019            NaN     True   \n",
              "A5                    Motor 4.0 Turbo  2019            NaN     True   \n",
              "J5                           Motor V6  2019            NaN     True   \n",
              "A3                       Motor 1.0 8v  2019            NaN     True   \n",
              "Série 1 M                    Motor V8  2019            NaN     True   \n",
              "...                               ...   ...            ...      ...   \n",
              "Lamborghini Reventón  Motor 4.0 Turbo  2019            NaN     True   \n",
              "Benni Mini                   Motor V8  2019            NaN     True   \n",
              "Uno                   Motor Diesel V6  2019            NaN     True   \n",
              "Santa Fe                Motor 3.0 32v  2019            NaN     True   \n",
              "XC60                  Motor 4.0 Turbo  2019            NaN     True   \n",
              "\n",
              "                                                             Acessórios  \\\n",
              "Nome                                                                      \n",
              "DS5                   ['Travas elétricas', '4 X 4', 'Vidros elétrico...   \n",
              "A5                    ['Câmbio automático', 'Câmera de estacionament...   \n",
              "J5                    ['Sensor crepuscular', 'Painel digital', 'Roda...   \n",
              "A3                    ['4 X 4', 'Piloto automático', 'Central multim...   \n",
              "Série 1 M             ['Controle de estabilidade', 'Central multimíd...   \n",
              "...                                                                 ...   \n",
              "Lamborghini Reventón  ['Controle de tração', 'Ar condicionado', 'Cen...   \n",
              "Benni Mini            ['Sensor crepuscular', 'Câmbio automático', 'C...   \n",
              "Uno                   ['Central multimídia', 'Sensor crepuscular', '...   \n",
              "Santa Fe              ['Travas elétricas', 'Ar condicionado', '4 X 4...   \n",
              "XC60                  ['Painel digital', 'Piloto automático', 'Centr...   \n",
              "\n",
              "                          Valor  \n",
              "Nome                             \n",
              "DS5                   124549.07  \n",
              "A5                     56445.20  \n",
              "J5                     53183.38  \n",
              "A3                     88552.39  \n",
              "Série 1 M              94564.40  \n",
              "...                         ...  \n",
              "Lamborghini Reventón   67664.86  \n",
              "Benni Mini            126247.84  \n",
              "Uno                   128852.21  \n",
              "Santa Fe              129415.33  \n",
              "XC60                   77675.79  \n",
              "\n",
              "[61 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-55248652-a236-4887-b6e9-6dd575ff9d13\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A5</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Câmbio automático', 'Câmera de estacionament...</td>\n",
              "      <td>56445.20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>J5</th>\n",
              "      <td>Motor V6</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor crepuscular', 'Painel digital', 'Roda...</td>\n",
              "      <td>53183.38</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A3</th>\n",
              "      <td>Motor 1.0 8v</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['4 X 4', 'Piloto automático', 'Central multim...</td>\n",
              "      <td>88552.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Série 1 M</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Controle de estabilidade', 'Central multimíd...</td>\n",
              "      <td>94564.40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Lamborghini Reventón</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Controle de tração', 'Ar condicionado', 'Cen...</td>\n",
              "      <td>67664.86</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Benni Mini</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor crepuscular', 'Câmbio automático', 'C...</td>\n",
              "      <td>126247.84</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Uno</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Central multimídia', 'Sensor crepuscular', '...</td>\n",
              "      <td>128852.21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Santa Fe</th>\n",
              "      <td>Motor 3.0 32v</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Ar condicionado', '4 X 4...</td>\n",
              "      <td>129415.33</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>XC60</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Painel digital', 'Piloto automático', 'Centr...</td>\n",
              "      <td>77675.79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>61 rows × 6 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-55248652-a236-4887-b6e9-6dd575ff9d13')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-55248652-a236-4887-b6e9-6dd575ff9d13 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-55248652-a236-4887-b6e9-6dd575ff9d13');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 361
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "DhlRbxy2D1Bd"
      },
      "source": [
        "#dataset.fillna(0) só altera a visualização "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OL04QU5RD1Be"
      },
      "source": [
        "dataset.fillna(0, inplace = True)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "fTH2JkGDD1Bf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "outputId": "b8f94fa4-0e7e-431e-b4b5-accb13528d14"
      },
      "source": [
        "dataset.query(\"Zero_km == True\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                Motor   Ano  Quilometragem  Zero_km  \\\n",
              "Nome                                                                  \n",
              "DS5                   Motor 2.4 Turbo  2019            0.0     True   \n",
              "A5                    Motor 4.0 Turbo  2019            0.0     True   \n",
              "J5                           Motor V6  2019            0.0     True   \n",
              "A3                       Motor 1.0 8v  2019            0.0     True   \n",
              "Série 1 M                    Motor V8  2019            0.0     True   \n",
              "...                               ...   ...            ...      ...   \n",
              "Lamborghini Reventón  Motor 4.0 Turbo  2019            0.0     True   \n",
              "Benni Mini                   Motor V8  2019            0.0     True   \n",
              "Uno                   Motor Diesel V6  2019            0.0     True   \n",
              "Santa Fe                Motor 3.0 32v  2019            0.0     True   \n",
              "XC60                  Motor 4.0 Turbo  2019            0.0     True   \n",
              "\n",
              "                                                             Acessórios  \\\n",
              "Nome                                                                      \n",
              "DS5                   ['Travas elétricas', '4 X 4', 'Vidros elétrico...   \n",
              "A5                    ['Câmbio automático', 'Câmera de estacionament...   \n",
              "J5                    ['Sensor crepuscular', 'Painel digital', 'Roda...   \n",
              "A3                    ['4 X 4', 'Piloto automático', 'Central multim...   \n",
              "Série 1 M             ['Controle de estabilidade', 'Central multimíd...   \n",
              "...                                                                 ...   \n",
              "Lamborghini Reventón  ['Controle de tração', 'Ar condicionado', 'Cen...   \n",
              "Benni Mini            ['Sensor crepuscular', 'Câmbio automático', 'C...   \n",
              "Uno                   ['Central multimídia', 'Sensor crepuscular', '...   \n",
              "Santa Fe              ['Travas elétricas', 'Ar condicionado', '4 X 4...   \n",
              "XC60                  ['Painel digital', 'Piloto automático', 'Centr...   \n",
              "\n",
              "                          Valor  \n",
              "Nome                             \n",
              "DS5                   124549.07  \n",
              "A5                     56445.20  \n",
              "J5                     53183.38  \n",
              "A3                     88552.39  \n",
              "Série 1 M              94564.40  \n",
              "...                         ...  \n",
              "Lamborghini Reventón   67664.86  \n",
              "Benni Mini            126247.84  \n",
              "Uno                   128852.21  \n",
              "Santa Fe              129415.33  \n",
              "XC60                   77675.79  \n",
              "\n",
              "[61 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-982f0663-2c32-4926-a8c3-43ace93602c4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Nome</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>DS5</th>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A5</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Câmbio automático', 'Câmera de estacionament...</td>\n",
              "      <td>56445.20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>J5</th>\n",
              "      <td>Motor V6</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor crepuscular', 'Painel digital', 'Roda...</td>\n",
              "      <td>53183.38</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A3</th>\n",
              "      <td>Motor 1.0 8v</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['4 X 4', 'Piloto automático', 'Central multim...</td>\n",
              "      <td>88552.39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Série 1 M</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Controle de estabilidade', 'Central multimíd...</td>\n",
              "      <td>94564.40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Lamborghini Reventón</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Controle de tração', 'Ar condicionado', 'Cen...</td>\n",
              "      <td>67664.86</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Benni Mini</th>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Sensor crepuscular', 'Câmbio automático', 'C...</td>\n",
              "      <td>126247.84</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Uno</th>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Central multimídia', 'Sensor crepuscular', '...</td>\n",
              "      <td>128852.21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Santa Fe</th>\n",
              "      <td>Motor 3.0 32v</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', 'Ar condicionado', '4 X 4...</td>\n",
              "      <td>129415.33</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>XC60</th>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>0.0</td>\n",
              "      <td>True</td>\n",
              "      <td>['Painel digital', 'Piloto automático', 'Centr...</td>\n",
              "      <td>77675.79</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>61 rows × 6 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-982f0663-2c32-4926-a8c3-43ace93602c4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-982f0663-2c32-4926-a8c3-43ace93602c4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-982f0663-2c32-4926-a8c3-43ace93602c4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 367
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lure2GvpD1Bg"
      },
      "source": [
        "dataset = pd.read_csv('db.csv', sep = ';')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4-ZvhXjvD1Bj",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "outputId": "cb940ddf-fef8-44d6-cbd3-689eed1dc8b6"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                      Nome                  Motor   Ano  Quilometragem  \\\n",
              "0            Jetta Variant        Motor 4.0 Turbo  2003        44410.0   \n",
              "1                   Passat           Motor Diesel  1991         5712.0   \n",
              "2                 Crossfox        Motor Diesel V8  1990        37123.0   \n",
              "3                      DS5        Motor 2.4 Turbo  2019            NaN   \n",
              "4         Aston Martin DB4        Motor 2.4 Turbo  2006        25757.0   \n",
              "..                     ...                    ...   ...            ...   \n",
              "253           Phantom 2013               Motor V8  2014        27505.0   \n",
              "254  Cadillac Ciel concept               Motor V8  1991        29981.0   \n",
              "255             Classe GLK  Motor 5.0 V8 Bi-Turbo  2002        52637.0   \n",
              "256       Aston Martin DB5           Motor Diesel  1996         7685.0   \n",
              "257                  Macan        Motor Diesel V6  1992        50188.0   \n",
              "\n",
              "     Zero_km                                         Acessórios      Valor  \n",
              "0      False  ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "1      False  ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "2      False  ['Piloto automático', 'Controle de estabilidad...   72832.16  \n",
              "3       True  ['Travas elétricas', '4 X 4', 'Vidros elétrico...  124549.07  \n",
              "4      False  ['Rodas de liga', '4 X 4', 'Central multimídia...   92612.10  \n",
              "..       ...                                                ...        ...  \n",
              "253    False  ['Controle de estabilidade', 'Piloto automátic...   51759.58  \n",
              "254    False  ['Bancos de couro', 'Painel digital', 'Sensor ...   51667.06  \n",
              "255    False  ['Rodas de liga', 'Controle de tração', 'Câmbi...   68934.03  \n",
              "256    False  ['Ar condicionado', '4 X 4', 'Câmbio automátic...  122110.90  \n",
              "257    False  ['Central multimídia', 'Teto panorâmico', 'Vid...   90381.47  \n",
              "\n",
              "[258 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c13cc09c-4988-4caf-86fe-d40c5890c1e4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>DS5</td>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2019</td>\n",
              "      <td>NaN</td>\n",
              "      <td>True</td>\n",
              "      <td>['Travas elétricas', '4 X 4', 'Vidros elétrico...</td>\n",
              "      <td>124549.07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Aston Martin DB4</td>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>253</th>\n",
              "      <td>Phantom 2013</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2014</td>\n",
              "      <td>27505.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Piloto automátic...</td>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>254</th>\n",
              "      <td>Cadillac Ciel concept</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>1991</td>\n",
              "      <td>29981.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Painel digital', 'Sensor ...</td>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>255</th>\n",
              "      <td>Classe GLK</td>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2002</td>\n",
              "      <td>52637.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Controle de tração', 'Câmbi...</td>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>256</th>\n",
              "      <td>Aston Martin DB5</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>257</th>\n",
              "      <td>Macan</td>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>1992</td>\n",
              "      <td>50188.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Vid...</td>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>258 rows × 7 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c13cc09c-4988-4caf-86fe-d40c5890c1e4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c13cc09c-4988-4caf-86fe-d40c5890c1e4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c13cc09c-4988-4caf-86fe-d40c5890c1e4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 369
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "MQUw7i1OD1Bk"
      },
      "source": [
        "dataset.dropna(subset =['Quilometragem'], inplace = True) #Para excluir um set de dados, como os NaN"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U4Cse7miD1Bl",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "outputId": "123836a7-d920-4716-edc0-3b6ff482c4d6"
      },
      "source": [
        "dataset"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                      Nome                  Motor   Ano  Quilometragem  \\\n",
              "0            Jetta Variant        Motor 4.0 Turbo  2003        44410.0   \n",
              "1                   Passat           Motor Diesel  1991         5712.0   \n",
              "2                 Crossfox        Motor Diesel V8  1990        37123.0   \n",
              "4         Aston Martin DB4        Motor 2.4 Turbo  2006        25757.0   \n",
              "5            Palio Weekend          Motor 1.8 16v  2012        10728.0   \n",
              "..                     ...                    ...   ...            ...   \n",
              "253           Phantom 2013               Motor V8  2014        27505.0   \n",
              "254  Cadillac Ciel concept               Motor V8  1991        29981.0   \n",
              "255             Classe GLK  Motor 5.0 V8 Bi-Turbo  2002        52637.0   \n",
              "256       Aston Martin DB5           Motor Diesel  1996         7685.0   \n",
              "257                  Macan        Motor Diesel V6  1992        50188.0   \n",
              "\n",
              "     Zero_km                                         Acessórios      Valor  \n",
              "0      False  ['Rodas de liga', 'Travas elétricas', 'Piloto ...   88078.64  \n",
              "1      False  ['Central multimídia', 'Teto panorâmico', 'Fre...  106161.94  \n",
              "2      False  ['Piloto automático', 'Controle de estabilidad...   72832.16  \n",
              "4      False  ['Rodas de liga', '4 X 4', 'Central multimídia...   92612.10  \n",
              "5      False  ['Sensor de estacionamento', 'Teto panorâmico'...   97497.73  \n",
              "..       ...                                                ...        ...  \n",
              "253    False  ['Controle de estabilidade', 'Piloto automátic...   51759.58  \n",
              "254    False  ['Bancos de couro', 'Painel digital', 'Sensor ...   51667.06  \n",
              "255    False  ['Rodas de liga', 'Controle de tração', 'Câmbi...   68934.03  \n",
              "256    False  ['Ar condicionado', '4 X 4', 'Câmbio automátic...  122110.90  \n",
              "257    False  ['Central multimídia', 'Teto panorâmico', 'Vid...   90381.47  \n",
              "\n",
              "[197 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-467a63cd-ae30-4d51-b94c-c7bf6f7491c3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Nome</th>\n",
              "      <th>Motor</th>\n",
              "      <th>Ano</th>\n",
              "      <th>Quilometragem</th>\n",
              "      <th>Zero_km</th>\n",
              "      <th>Acessórios</th>\n",
              "      <th>Valor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jetta Variant</td>\n",
              "      <td>Motor 4.0 Turbo</td>\n",
              "      <td>2003</td>\n",
              "      <td>44410.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Travas elétricas', 'Piloto ...</td>\n",
              "      <td>88078.64</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Passat</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1991</td>\n",
              "      <td>5712.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Fre...</td>\n",
              "      <td>106161.94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Crossfox</td>\n",
              "      <td>Motor Diesel V8</td>\n",
              "      <td>1990</td>\n",
              "      <td>37123.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Piloto automático', 'Controle de estabilidad...</td>\n",
              "      <td>72832.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Aston Martin DB4</td>\n",
              "      <td>Motor 2.4 Turbo</td>\n",
              "      <td>2006</td>\n",
              "      <td>25757.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', '4 X 4', 'Central multimídia...</td>\n",
              "      <td>92612.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Palio Weekend</td>\n",
              "      <td>Motor 1.8 16v</td>\n",
              "      <td>2012</td>\n",
              "      <td>10728.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Sensor de estacionamento', 'Teto panorâmico'...</td>\n",
              "      <td>97497.73</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>253</th>\n",
              "      <td>Phantom 2013</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>2014</td>\n",
              "      <td>27505.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Controle de estabilidade', 'Piloto automátic...</td>\n",
              "      <td>51759.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>254</th>\n",
              "      <td>Cadillac Ciel concept</td>\n",
              "      <td>Motor V8</td>\n",
              "      <td>1991</td>\n",
              "      <td>29981.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Bancos de couro', 'Painel digital', 'Sensor ...</td>\n",
              "      <td>51667.06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>255</th>\n",
              "      <td>Classe GLK</td>\n",
              "      <td>Motor 5.0 V8 Bi-Turbo</td>\n",
              "      <td>2002</td>\n",
              "      <td>52637.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Rodas de liga', 'Controle de tração', 'Câmbi...</td>\n",
              "      <td>68934.03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>256</th>\n",
              "      <td>Aston Martin DB5</td>\n",
              "      <td>Motor Diesel</td>\n",
              "      <td>1996</td>\n",
              "      <td>7685.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Ar condicionado', '4 X 4', 'Câmbio automátic...</td>\n",
              "      <td>122110.90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>257</th>\n",
              "      <td>Macan</td>\n",
              "      <td>Motor Diesel V6</td>\n",
              "      <td>1992</td>\n",
              "      <td>50188.0</td>\n",
              "      <td>False</td>\n",
              "      <td>['Central multimídia', 'Teto panorâmico', 'Vid...</td>\n",
              "      <td>90381.47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>197 rows × 7 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-467a63cd-ae30-4d51-b94c-c7bf6f7491c3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-467a63cd-ae30-4d51-b94c-c7bf6f7491c3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-467a63cd-ae30-4d51-b94c-c7bf6f7491c3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 373
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "8L4wum05D1Bl"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8iLOc-U3D1Bm"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Goodbye World!\n"
      ],
      "metadata": {
        "id": "JUpkSWUItNGl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib as mpl"
      ],
      "metadata": {
        "id": "3Nbh1cAVud4t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataset = pd.DataFrame({'Pal' : 'Goodbye World', \"symb\": '!!!!!!'}, index = [0])"
      ],
      "metadata": {
        "id": "DRV1wLtEvL2e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "BjOQ_V0mvREN",
        "outputId": "14c2cf49-9d30-407e-8341-bbce57879e38"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             Pal    symb\n",
              "0  Goodbye World  !!!!!!"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-77a32a72-3b97-43a6-9f8e-0b693ca9d0e4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Pal</th>\n",
              "      <th>symb</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Goodbye World</td>\n",
              "      <td>!!!!!!</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-77a32a72-3b97-43a6-9f8e-0b693ca9d0e4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-77a32a72-3b97-43a6-9f8e-0b693ca9d0e4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-77a32a72-3b97-43a6-9f8e-0b693ca9d0e4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 357
        }
      ]
    }
  ]
}