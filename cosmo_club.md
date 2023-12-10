# cosmology club


## 观测计划

### 玻尔兹曼方程

- 时间：2023-12-6 19:00-21:00 
- 地点：S621
- 讨论内容：徐文硕主讲 Daniel Baumann - Cosmology (2021) 6.1节 P215-231 Linear Perturbations Evolution equation in Newtonian gauge.


## 记录

### 2023-10-16: expansion

**宇宙膨胀相关概念回顾**
- 集中尝试：2023-10-25 19:00-21:00 地点S621
- 集中讨论：2023-11-1 19:00-21:00 地点S621
  - 参与者：赵成老师、芝士鱼、太阳鱼、zyjj、gsh、syt、zyf、xrjj、jnjj
- 材料：
  - code/expansion.ipynb
  - notes/expansion

请完成以下5道判断题。先尝试用物理图像判断，如有必要可以计算和画图，最后再借助计算和画图结果用物理图像判断。
1. 只有暴涨时期宇宙膨胀速度会超光速
   1. $\dot{a} >1$. 
   2. 退行速度
2. 存在退行速度超光速的天体，但我们没法观测到
   1. Hubble sphere 外，lightcone上。
3. 暴涨结束以后，宇宙的膨胀速度（本动速度为0的天体的退行速度）单调递增 (这题和后面的题都基于现在的标准宇宙学模型，即flat-LCDM，Omega_m在0.3左右，H0在70左右)
   1. $\ddot{a} = -\frac{4\pi}{3} G(\rho + 3P )a$
      1. matter dominate, $P=0$, $\ddot{a}<0$
      2. D.E. dominate, $P=-\rho$, $\ddot{a}>0$. 
4. 当被我们接受到的天体光线发出时，其退行速度一定小于光速。
5. 如果一个天体现在的退行速度大于或等于光速，那么它现在发出的光永远不会被我们看到。
   1. Event horizon compare with the Hubble sphere at z=0.
   2. Event horizon will be shown more clearly and meaningfully in the conformal time plot.

### 2023-11-15: pertubation in GR

- 时间：2023-11-15 19:00-21:00 
- 地点：S621
- 参与者：徐睿（主讲）、丹丹、太阳鱼、xws、gsh、芝士鱼、zyf
- 内容：
  - 回顾了宇宙学的均匀背景
  - 讨论perturbation和guage transformation

### 2023-11-22：玻尔兹曼方程

- 时间：2023-11-22 19:00-22:00 
- 地点：S621
- 参与者：徐睿（主讲）、刘肇宁、姜春阳、褚佳妮、徐文硕、马庆麟、张遥、芝士鱼、苟诗涵、丹丹、王正一、靖长成、苏雨桐、杨晓睿、太阳鱼
- 讨论内容：徐睿主讲玻尔兹曼方程，课件见 `refs/cmbeqs.pdf`

### 2023-11-29: 间奏

- 时间：2023-11-29 19:00-22:00 
- 地点：S621
- 参与者：徐睿、徐文硕、马庆麟、芝士鱼、苟诗涵、杨晓睿、太阳鱼、褚佳妮

讨论内容：
1. 习题课（赵成老师的两道题）
   1. vector perturbation 为什么不重要？（讨论摘要：Baumann书上有提到vector perturbation会衰减，实际上这个结论需要自己计算一下 vector perturbation 的演化方程，且手算难度较大——之后计划看看 Baumann 的 mathematica notebook。）
   2. 一阶的 tensor perturbation 是不是 gauge- invariant （讨论摘要：gauge- invariant 要求所有分量在坐标变换下不变，Baumann 书的 6.18-6.21式展示了结果，tensor perturbation 是 gauge- invariant的，之后要自己算一遍。）
2. 芝士鱼主讲 Daniel Baumann - Cosmology (2021)  P210-215，摘要：（原则上看了这个摘要就不用看这几页书了（x）
   1. Baumann这本书第五章讲 classical 的 （牛顿引力框架下的） perturbation theory，第六章开头指出，牛顿框架下的推导有两个问题：
      1. 不适用于超过 Hubble radius 的大尺度。事实上 后面会看到 牛顿版本的 perturbation theory 是 Relativistic perturbation theory 在小尺度的简化。
      2. 不适用于 photon，neutrino 等相对论流体。
   2. 第六章主要有三部分：
      1. 6.1 节 derive the linearized evolution equations in Newtonian gauge
      2. 6.2 节讨论  initial conditions of perturbations of superhorizon scales
      3. 6.3 节和 6.4 节讨论  observed correlations
   3. 在 6.1 节开头，Baumann 表述了和赵成老师类似的想法：perturbation theory 的物理图象是简单的，它之所以有“难”的名声是因为 1） tensor 的代数有点麻烦， 2） gauge problem，通过 坐标系的选取，matter perturbations 可以转化为 metric perturbations。
   4. 6.1.1 节：
      1. 写下一个 general 的 metric perturbation $$\mathrm{d} s^2=a^2(\eta)\left[-(1+2 A) \mathrm{d} \eta^2+2 B_i \mathrm{~d} x^i \mathrm{~d} \eta+\left(\delta_{i j}+2 E_{i j}\right) \mathrm{d} x^i \mathrm{~d} x^j\right]$$ 
      2. 对它做 scalar-vector-tensor (SVT) 分解，得到
         1. 4 scalar perturbations: $A$, $B$, $C$, $E$
         2. 2 *divergenceless* vector (DoF=2) perturbations: $\hat{B}_i, \hat{E}_i$ 
         3. 1 *divergenceless and traceless* tensor (DoF=2) perturbations: $\hat{E}_{i j}$
      3. SVT 分解的依据是：在 linear order 它们各自演化，不会 mix
         1. comment: 这个还挺常用的，计算inflation期间的态演化也会用类似的分解。
      4. gauge problem
         1. $\hat{B}_i$ 和 $\hat{E}_i$ 是 gauge-dependent. 在更改空间坐标 $x^i \mapsto \tilde{x}^i=x^i+\xi^i(\eta, \mathbf{x})$ 的变换下可以得到 $B_i=-\xi_i^{\prime}$ and $\hat{E}_i=-\xi_i$，其中 $\xi_i$ 就是坐标变化带来的假 perturbation.
         2. energy density perturbation 可以通过 conformal time 的变换 $\eta \mapsto \tilde{\eta}=\eta+\xi^0(\eta, \mathbf{x})$ 转移到度规里。
         3. gauge problem 的解决办法：
            1. 寻找 gauge invariant variables
            2. 固定 gauge 计算，最后算到观测量。
3. 商定接下来读 Daniel Baumann - Cosmology (2021) 第六章，perturbation theory 的广相部分。
   1. 读法：轮流领读，提倡大家都在讨论前看阅读材料并自己推导。
   2. 背景说明和后续：前两次徐睿讲的是该书附录B，perturbation theory 的 玻尔兹曼方程部分。我们读完第六章后可能会接着读第七章，即如何与观测数据相联系。
   3. 其它补充材料：
      1. 徐睿推荐论文 https://arxiv.org/abs/astro-ph/0606683v1 ，考虑作为读书完成后的复习材料。
      2. Baumann在第六章开头提到了编程计（经典的code如 [CLASS](http://class-code.net) 和 [CAMB](http://camb.info) ）对于理解内容的帮助，并给出了他自己的 [mathematica notebook](https://www.cambridge.org/highereducation/books/cosmology/53783DD7B3CB15E2E37ADFBC0C1B930F/resources/student-resources/B3B89707FBB9F95DE18310093A529228/code/7ADC482827F380882EAFABD64F607393)，可以在读书的时候参考。


### plan: linear PS

- 本学期（2023年秋）拟定计算linear power spectrum（包括基础知识的复习、数值求解玻尔兹曼方程，之后可以通过各种transfer function转化成可以和观测比较的形式）

赵成老师的说明：线性功率谱是几乎所有宇宙大尺度研究的基础，提供了宇宙结构形成的初条件。结构形成理论、数值模拟、大尺度probe的数据拟合都是以线性功率谱为基础，所以线性功率谱在宇宙学中的地位非常重要。
当然，从第一性原理开始，算出线性功率谱并不容易。除了理论功底外，对编程能力也是一个考验。日常生活中，除了研究非标准宇宙学理论的，一般也不需要从头开始。大部分情况下这可能属于“一辈子只做一次”的事情。
另外给几个参考文献：
1. [Easy] https://pycosmohub.com/hub （现成的宇宙学工具包，python写的，而且比较新），包括其微扰论计算相关的文章 https://arxiv.org/abs/1708.05177 (and references therein)。这个工具包并没有self-contained，比如recombination方面的计算依赖的是recfast。但这样便于你们略过微观理论的细节、集中于宇宙学基本原理相关的计算上。必要的时候也可以参考 PyCosmo 的实现。
2. [Medium] https://camb.info/theory.html 中的一些 Maple 示例。此外，也有 Mathematica 和 Jupyter notebook 可以参考：https://camb.info/jrs/ ， https://camb.readthedocs.io/en/latest/ScalEqs.html
3. [Hard] https://cosmologist.info/notes/thesis.pdf （Antony 的博士论文），以及 https://camb.info/readme.html#Refs 列出的参考文献
4. [Insane] https://arxiv.org/abs/astro-ph/9506072 (微扰理论的黄金教材，现代宇宙学的皇冠明珠，脑科体操的不二之选)



## Todo list 

- [ ] what is CMB scale? Which kind of observation can probe the end of inflation?
- [ ] tensor perturbation 为什么是引力波？