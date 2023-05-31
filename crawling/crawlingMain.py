{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO+rYF0CD1MQCpdIEgHdx2w",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/JaehyeongWang/swe3032_team7/blob/yuha/crawling/crawlingMain.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZIyPhqFomoqB",
        "outputId": "2a0cedbf-1ebe-4512-e1cb-03c91d778aae"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### git"
      ],
      "metadata": {
        "id": "XAZZGtgb-IhS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cd /content/drive/MyDrive/인지프230531"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Arp6Gpj4-W2g",
        "outputId": "a93c60b1-35b3-493e-ee77-f018c40de7b3"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/인지프230531\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git config --global user.email \"yuuhaaaaa19@gmail.com\"\n",
        "!git config --global user.name \"yuuhaaaaa\""
      ],
      "metadata": {
        "id": "iS62wCtF-ZCR"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git config --list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wtwz1EQl-cDe",
        "outputId": "2c93981e-657e-481e-e684-0c1d6a852026"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "filter.lfs.clean=git-lfs clean -- %f\n",
            "filter.lfs.smudge=git-lfs smudge -- %f\n",
            "filter.lfs.process=git-lfs filter-process\n",
            "filter.lfs.required=true\n",
            "user.email=yuuhaaaaa19@gmail.com\n",
            "user.name=yuuhaaaaa\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git init"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pKJihx_Q-dpu",
        "outputId": "bbbbd84f-a312-49fc-84da-9a1c0fb075ad"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Initialized empty Git repository in /content/drive/MyDrive/인지프230531/.git/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git remote add origin https://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@github.com/JaehyeongWang/swe3032_team7.git"
      ],
      "metadata": {
        "id": "Fndp7g3v-e5Z"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git remote -v"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7vMzaT3l-huw",
        "outputId": "3d5bcf84-13a3-444d-b1d2-69e023af5ab9"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "origin\thttps://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@github.com/JaehyeongWang/swe3032_team7.git (fetch)\n",
            "origin\thttps://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@github.com/JaehyeongWang/swe3032_team7.git (push)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git remote update"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZmUwuEsp-ix9",
        "outputId": "a3046460-0cfc-4732-e1bc-d8c07f0450f9"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fetching origin\n",
            "remote: Enumerating objects: 389, done.\u001b[K\n",
            "remote: Counting objects: 100% (53/53), done.\u001b[K\n",
            "remote: Compressing objects: 100% (47/47), done.\u001b[K\n",
            "remote: Total 389 (delta 19), reused 7 (delta 2), pack-reused 336\u001b[K\n",
            "Receiving objects: 100% (389/389), 8.23 MiB | 11.33 MiB/s, done.\n",
            "Resolving deltas: 100% (148/148), done.\n",
            "From https://github.com/JaehyeongWang/swe3032_team7\n",
            " * [new branch]      hyein      -> origin/hyein\n",
            " * [new branch]      jaehyeong  -> origin/jaehyeong\n",
            " * [new branch]      jaehyun    -> origin/jaehyun\n",
            " * [new branch]      main       -> origin/main\n",
            " * [new branch]      yuha       -> origin/yuha\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git checkout main"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uwEISuh1-j0b",
        "outputId": "172a8910-6459-4729-8539-3fe9f6ca45d6"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Branch 'main' set up to track remote branch 'main' from 'origin'.\n",
            "Switched to a new branch 'main'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git branch"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B5_Zt18q-lBN",
        "outputId": "65daa733-9b76-403a-c492-8ca8feef2823"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* \u001b[32mmain\u001b[m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git pull origin main"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uWI2iLf7nS5U",
        "outputId": "1a51f905-871d-4430-d94d-5031e5fb8b98"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "From https://github.com/JaehyeongWang/swe3032_team7\n",
            " * branch            main       -> FETCH_HEAD\n",
            "Already up to date.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git checkout yuha"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bR_0Ev9pnW1q",
        "outputId": "d356705d-b91b-49bd-d226-c60868cb761b"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Branch 'yuha' set up to track remote branch 'yuha' from 'origin'.\n",
            "Switched to a new branch 'yuha'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git merge main"
      ],
      "metadata": {
        "id": "_6aeipTM-nik",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "da33bfb0-7f56-46fc-d4a5-fb120a18b2d6"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "error: Merging is not possible because you have unmerged files.\n",
            "\u001b[33mhint: Fix them up in the work tree, and then use 'git add/rm <file>'\u001b[m\n",
            "\u001b[33mhint: as appropriate to mark resolution and make a commit.\u001b[m\n",
            "fatal: Exiting because of an unresolved conflict.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2yNYoScdps_h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''!git reset\n",
        "!git checkout .\n",
        "!git clean -fdx'''"
      ],
      "metadata": {
        "id": "fHh7Xj0--mXk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''!git add .\n",
        "!git commit -m 'update for local use'\n",
        "!git push --set-upstream origin yuha'''"
      ],
      "metadata": {
        "id": "FIiEf6t2-qy_"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}