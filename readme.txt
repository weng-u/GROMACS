
!!!非正式，自己在做多副本分子动力学模拟时请不要轻易使用这里所提供的mdp文件（正式的mdp文件和步骤请夏元铃整理）！！！

分子动力学模拟过程及简单原理请参见Justin A. Lemkul的教程 http://www.mdtutorials.com/gmx/lysozyme/index.html

GROMACS参数说明（Molecular dynamics parameters (.mdp options)）请参见：
http://manual.gromacs.org/documentation/5.1/user-guide/mdp-options.html#mdp-value-vdwtype=Cut-off

GROMACS Command-line reference（或工具说明）请参见：
http://manual.gromacs.org/documentation/5.1/user-guide/cmdline.html

这里以unliganded gp120和gp120-CD4 complex为模拟对象，对它们各自进行了10次100 ns的多副本分子动力学模拟。具体步骤为：
结构坐标的获得->蛋白质-溶剂体系的准备（pdb2gmx，加水，加离子）-> 能量最小化处理->位置限制性分子动力学模拟（或平衡模拟。共4次，前三次为NVT equilibration,最后一次为NPT 
equilibration）-> 10次生产分子动力学模拟。

注意：
1. 这里并没有提供真空中、加水后、加锂离子后能量最小化的mdp文件，仅仅是在蛋白质-溶剂（包含NaCl）体系彻底构建完毕之后进行了一次能量最小化处理；
2. 范德华力的处理方式为twin-range cut-offs (以后实验室进行常规分子动力学模拟时，对范德华力的处理均使用switch函数方式，请夏远铃整理)
2. 位置限制性模拟的第一次依照Maxwell分布在300 K下生成了原子速度，之后的三次均不生成原子速度，模拟起始时的原子速度来自上一次模拟结束时的速度，通过grompp读取存储于
上一次模拟结束时的.gro或.cpt文件中；
3. 10次多副本生产动力学模拟，每次都要随机生成300 K下的原子速度。

以下为英文步骤说明（具体的中文步骤，包含真空中和加水后的能量优化mdp文件，如何使用switch function处理范德华力，请夏远铃补充后最为最终的范本）。

Molecular dynamics (MD) simulation procedure and involved files：

Upon obtaining the coordinate files for the unliganded gp120 (unliganded_gp120.pdb) and gp120-CD4 complex (gp120-CD4.pdb), the initial topology files were created by the
GROMACS tool ‘gmx pdb2gmx’. After defining the box dimensions (using the ‘gmx editconf’ tool), filling the box with water (using the ‘gmx solvate’ tool), and adding Cl^-1 
and Na^+ ions to the system (using the “gmx genion” tool), we obtained the final topology files (unliganded_gp120.top and gp120-CD4.top) and the solvated, electroneutral
protein-solvent systems at a salt concentration of 150 mM for the unliganded gp120 and gp120-CD4 complex. 

Subsequently, each system was subjected to the steepest descent energy minimization (EM), where the binary input was generated using the ‘gmx grompp’ tool with 
minim.mdp as the input parameter file, followed by running the EM through the GROMACS MD engine, ‘gmx mdrun’.  Equilibration of the solvent and ions around the solute 
(i.e., the protein) was accomplished by four consecutive 200-ps position-restrained MD simulations, for which the gradually decreasing force constants exerted on the 
protein heavy atoms, i.e., Kposres = 1000, 100, 10, and 0 kJ mol1 nm2, were obtained using the ‘gmx genrestr’ tool, respectively, and the input parameter files used 
for generating the binary inputs were equil1.mdp, equil2.mdp, equil3.mdp, and equil4.mdp, respectively. Note that when executing the ‘grompp’ to generate the inputs for 
the last three position-restrained MD runs, the -t flag was included to include the checkpoint file (from which the coordinates and velocities were read) from the 
previous equilibration. After equilibration, each system was subjected to 10 independent 100-ns production MD runs, with each of them being initializing with different 
initial atomic velocities generated using different random seeds, which assigned the initial velocities in ‘gmx grompp’ according to a Maxwell distribution at 300 K 
(for details, see parameters continuation = no, gen-vel = yes, gen-temp = 300, and gen-seed = -1 in the file md.mdp). 


