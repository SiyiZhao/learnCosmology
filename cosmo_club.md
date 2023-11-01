# cosmology club


## 观测计划

2023-10-16：**宇宙膨胀相关概念回顾**
- 集中尝试：2023-10-25 19:00-21:00 地点S621
- 集中讨论：2023-11-1 19:00-21:00 地点S621

请完成以下5道判断题。先尝试用物理图像判断，如有必要可以计算和画图，最后再借助计算和画图结果用物理图像判断。
1. 只有暴涨时期宇宙膨胀速度会超光速
   1. $\dot{a} >1$. 
2. 存在退行速度超光速的天体，但我们没法观测到
   1. Hubble sphere 外，lightcone上。
3. 暴涨结束以后，宇宙的膨胀速度（本动速度为0的天体的退行速度）单调递增 (这题和后面的题都基于现在的标准宇宙学模型，即flat-LCDM，Omega_m在0.3左右，H0在70左右)
   1. $\ddot{a}$
4. 当被我们接受到的天体光线发出时，其退行速度一定小于光速。
5. 如果一个天体现在的退行速度大于或等于光速，那么它现在发出的光永远不会被我们看到。
   1. Event horizon compare with the Hubble sphere at z=0.
   2. Event horizon will be shown more clearly and meaningfully in the conformal time plot.




## Todo list 

- [ ] what is CMB scale? Which kind of observation can probe the end of inflation?

## 记录

- 本学期（2023年秋）拟定计算linear power spectrum（包括基础知识的复习、数值求解玻尔兹曼方程，之后可以通过各种transfer function转化成可以和观测比较的形式）

赵成老师的说明：线性功率谱是几乎所有宇宙大尺度研究的基础，提供了宇宙结构形成的初条件。结构形成理论、数值模拟、大尺度probe的数据拟合都是以线性功率谱为基础，所以线性功率谱在宇宙学中的地位非常重要。
当然，从第一性原理开始，算出线性功率谱并不容易。除了理论功底外，对编程能力也是一个考验。日常生活中，除了研究非标准宇宙学理论的，一般也不需要从头开始。大部分情况下这可能属于“一辈子只做一次”的事情。
另外给几个参考文献：
1. [Easy] https://pycosmohub.com/hub （现成的宇宙学工具包，python写的，而且比较新），包括其微扰论计算相关的文章 https://arxiv.org/abs/1708.05177 (and references therein)。这个工具包并没有self-contained，比如recombination方面的计算依赖的是recfast。但这样便于你们略过微观理论的细节、集中于宇宙学基本原理相关的计算上。必要的时候也可以参考 PyCosmo 的实现。
2. [Medium] https://camb.info/theory.html 中的一些 Maple 示例。此外，也有 Mathematica 和 Jupyter notebook 可以参考：https://camb.info/jrs/ ， https://camb.readthedocs.io/en/latest/ScalEqs.html
3. [Hard] https://cosmologist.info/notes/thesis.pdf （Antony 的博士论文），以及 https://camb.info/readme.html#Refs 列出的参考文献
4. [Insane] https://arxiv.org/abs/astro-ph/9506072 (微扰理论的黄金教材，现代宇宙学的皇冠明珠，脑科体操的不二之选)
