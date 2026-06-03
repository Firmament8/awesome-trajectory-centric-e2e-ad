# Awesome Trajectory-Centric End-to-End Autonomous Driving

A curated literature list for trajectory-centric end-to-end autonomous driving under planning-oriented evaluation, with emphasis on BEV representations, VLM/VLA reasoning, world models, rollout-based planning, and benchmarks such as NAVSIM.

This repository is organized as a public reading map rather than a claim of exhaustive coverage. The first version is generated from the BibTeX references of the survey manuscript:

> An Overview of Trajectory-Centric End-to-End Autonomous Driving under Planning-Oriented Evaluation for AI-Enabled Transportation Systems

## Maintenance Notes

Paper metadata is generated from `bibliography/references.bib`. DOI, arXiv, and URL links are shown when they are present in the BibTeX source; entries without a direct link are marked as search-only. Code, project, and dataset links can be added later after checking the paper page, author page, or official repository.

## Contents

- [Surveys and Positioning](#surveys-and-positioning)
- [VLM, VLA, Language, and Reasoning](#vlm-vla-language-and-reasoning)
- [World Models, Rollout, and Generative Simulation](#world-models-rollout-and-generative-simulation)
- [Planning-Oriented Evaluation and Benchmarks](#planning-oriented-evaluation-and-benchmarks)
- [BEV, Occupancy, and Perception](#bev-occupancy-and-perception)
- [Trajectory Prediction and End-to-End Planning](#trajectory-prediction-and-end-to-end-planning)
- [Background: Intelligent Transportation and Autonomous Driving](#background-intelligent-transportation-and-autonomous-driving)
- [Other Relevant Papers](#other-relevant-papers)

## Visual Map

The following figures are copied from the survey assets for navigation and topic organization.

![Trajectory-centric evolution](assets/figures/from_open_loop_to_trajectory_centric_e2e.png)

![BEV paradigms](assets/figures/bev.png)

![VLM and VLA roles](assets/figures/vlm.png)

![World-model taxonomy](assets/figures/World_Model_Taxonomy_in_Autonomous_Driving.png)

## Paper List

<!-- BEGIN PAPER_LIST -->

Generated from `bibliography/references.bib`. DOI, arXiv, and URL links are derived only from explicit BibTeX fields. Entries marked `search only` do not yet have a verified direct paper/project/code link in this repository.

## Surveys and Positioning

- **The role of world models in shaping autonomous driving: A comprehensive survey**. Tu, Sifan et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2502.10498) `bib:tu2025role`
- **Large Foundation Models for Trajectory Prediction in Autonomous Driving: A Comprehensive Survey**. Dai, Wei et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2509.10570) `bib:dai2025lfm_traj_survey`
- **Grid-Centric Traffic Scenario Perception for Autonomous Driving: A Comprehensive Review**. Shi, Yining et al., IEEE Trans. Neural Netw. Learn. Syst., 2025. [[DOI]](https://doi.org/10.1109/TNNLS.2024.3495045) `bib:shi2024grid`
- **CoVLA: Comprehensive vision-language-action dataset for autonomous driving**. Arai, Hidehisa et al., Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. (WACV), 2025. [search only](https://scholar.google.com/scholar?q=CoVLA%3A+Comprehensive+vision-language-action+dataset+for+autonomous+driving) `bib:arai2025covla`
- **A survey of world models for autonomous driving**. Feng, Tuo et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2501.11260) `bib:feng2025survey`
- **A survey of autonomous driving from a deep learning perspective**. Zhao, Jingyuan et al., ACM Comput. Surv., 2025. [search only](https://scholar.google.com/scholar?q=A+survey+of+autonomous+driving+from+a+deep+learning+perspective) `bib:zhao2025survey`
- **A Survey on Vision-Language-Action Models for Autonomous Driving**. Jiang, Sicong et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshops (ICCVW), 2025. [[DOI]](https://doi.org/10.1109/ICCVW69036.2025.00476) `bib:jiang2025vla4ad_survey`
- **Vision-language models for vision tasks: A survey**. Zhang, Jingyi et al., IEEE Trans. Pattern Anal. Mach. Intell., 2024. [search only](https://scholar.google.com/scholar?q=Vision-language+models+for+vision+tasks%3A+A+survey) `bib:zhang2024vision`
- **End-to-end autonomous driving: Challenges and frontiers**. Chen, Li et al., IEEE Trans. Pattern Anal. Mach. Intell., 2024. [[DOI]](https://doi.org/10.1109/TPAMI.2024.3435937) `bib:chen2024end`
- **A Survey on Multimodal Large Language Models for Autonomous Driving**. Cui, Can et al., Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. Workshops (WACVW), 2024. [[DOI]](https://doi.org/10.1109/WACVW60836.2024.00106) `bib:cui2023mllm_survey`
- **Recent advancements in end-to-end autonomous driving using deep learning: A survey**. Chib, Pranav Singh et al., IEEE Trans. Intell. Vehicles, 2023. [search only](https://scholar.google.com/scholar?q=Recent+advancements+in+end-to-end+autonomous+driving+using+deep+learning%3A+A+survey) `bib:chib2023recent`
- **Traffic prediction using artificial intelligence: Review of recent advances and emerging opportunities**. Shaygan, Maryam et al., Transportation Research Part C: Emerging Technologies, 2022. [[DOI]](https://doi.org/10.1016/j.trc.2022.103921) `bib:shaygan2022trafficprediction`
- **Milestones in autonomous driving and intelligent vehicles: Survey of surveys**. Chen, Long et al., IEEE Trans. Intell. Vehicles, 2022. [search only](https://scholar.google.com/scholar?q=Milestones+in+autonomous+driving+and+intelligent+vehicles%3A+Survey+of+surveys) `bib:chen2022milestones`
- **A survey on autonomous vehicle control in the era of mixed-autonomy: From physics-based to AI-guided driving policy learning**. Di, Xuan et al., Transportation Research Part C: Emerging Technologies, 2021. [[DOI]](https://doi.org/10.1016/j.trc.2021.103008) `bib:di2021mixedautonomy`

## VLM, VLA, Language, and Reasoning

- **ReCogDrive: A reinforced cognitive framework for end-to-end autonomous driving**. Li, Yongkang et al., Proc. Int. Conf. Learn. Represent. (ICLR), 2026. [search only](https://scholar.google.com/scholar?q=ReCogDrive%3A+A+reinforced+cognitive+framework+for+end-to-end+autonomous+driving) `bib:li2025recogdrive`
- **OpenDriveVLA: Towards end-to-end autonomous driving with large vision-language-action model**. Zhou, Xingcheng et al., Proc. AAAI Conf. Artif. Intell., 2026. [[DOI]](https://doi.org/10.1609/AAAI.V40I16.38386) `bib:zhou2025opendrivevlaendtoendautonomousdriving`
- **DriveWorld-VLA: Unified latent-space world modeling with vision-language-action for autonomous driving**. Liu, Lin et al., misc, 2026. [[arXiv]](https://arxiv.org/abs/2602.06521) `bib:liu2026driveworld`
- **DriveVLA-W0: World models amplify data scaling law in autonomous driving**. Li, Yingyan et al., Proc. Int. Conf. Learn. Represent. (ICLR), 2026. [search only](https://scholar.google.com/scholar?q=DriveVLA-W0%3A+World+models+amplify+data+scaling+law+in+autonomous+driving) `bib:li2025drivevla`
- **WorldVLA: Towards Autoregressive Action World Model**. Cen, Jun et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2506.21539) `bib:cen2025worldvla`
- **TinyVLA: Towards fast, data-efficient vision-language-action models for robotic manipulation**. Wen, Junjie et al., IEEE Robot. Autom. Lett., 2025. [[DOI]](https://doi.org/10.1109/LRA.2025.3544909) `bib:wen2025tinyvla`
- **SimLingo: Vision-only closed-loop autonomous driving with language-action alignment**. Renz, Katrin et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [search only](https://scholar.google.com/scholar?q=SimLingo%3A+Vision-only+closed-loop+autonomous+driving+with+language-action+alignment) `bib:renz2025simlingo`
- **OmniDrive: A holistic vision-language dataset for autonomous driving with counterfactual reasoning**. Wang, Shihao et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [search only](https://scholar.google.com/scholar?q=OmniDrive%3A+A+holistic+vision-language+dataset+for+autonomous+driving+with+counterfactual+reasoning) `bib:wang2025omnidrive`
- **Learning to Act Anywhere with Task-centric Latent Actions**. Bu, Qingwen et al., Proc. Robot.: Sci. Syst. (RSS), 2025. [[DOI]](https://doi.org/10.15607/RSS.2025.XXI.014) `bib:bu2025univla`
- **DrivingGPT: Unifying driving world modeling and planning with multi-modal autoregressive transformers**. Chen, Yuntao et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=DrivingGPT%3A+Unifying+driving+world+modeling+and+planning+with+multi-modal+autoregressive+transformers) `bib:chen2025drivinggpt`
- **DriveGPT4-V2: Harnessing large language model capabilities for enhanced closed-loop autonomous driving**. Xu, Zhenhua et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [search only](https://scholar.google.com/scholar?q=DriveGPT4-V2%3A+Harnessing+large+language+model+capabilities+for+enhanced+closed-loop+autonomous+driving) `bib:xu2025drivegpt4`
- **DriveDreamer-2: LLM-enhanced world models for diverse driving video generation**. Zhao, Guosheng et al., Proc. AAAI Conf. Artif. Intell., 2025. [search only](https://scholar.google.com/scholar?q=DriveDreamer-2%3A+LLM-enhanced+world+models+for+diverse+driving+video+generation) `bib:zhao2025drivedreamer`
- **AutoVLA: A vision-language-action model for end-to-end autonomous driving with adaptive reasoning and reinforcement fine-tuning**. Zhou, Zewei et al., Proc. Adv. Neural Inf. Process. Syst., 2025. [search only](https://scholar.google.com/scholar?q=AutoVLA%3A+A+vision-language-action+model+for+end-to-end+autonomous+driving+with+adaptive+reasoning+and+reinforcement+fine-tuning) `bib:zhou2025autovla`
- **Vision-language model-driven scene understanding and robotic object manipulation**. Liu, Sichao et al., Proc. IEEE Int. Conf. Autom. Sci. Eng. (CASE), 2024. [search only](https://scholar.google.com/scholar?q=Vision-language+model-driven+scene+understanding+and+robotic+object+manipulation) `bib:liu2024vision`
- **VLP: Vision-language planning for autonomous driving**. Pan, Chenbin et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=VLP%3A+Vision-language+planning+for+autonomous+driving) `bib:pan2024vlp`
- **VLAI: Exploration and exploitation based on visual-language aligned information for robotic object goal navigation**. Luo, Haonan et al., Image Vis. Comput., 2024. [search only](https://scholar.google.com/scholar?q=VLAI%3A+Exploration+and+exploitation+based+on+visual-language+aligned+information+for+robotic+object+goal+navigation) `bib:luo2024vlai`
- **Taskclip: Extend large vision-language model for task oriented object detection**. Chen, Hanning et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Taskclip%3A+Extend+large+vision-language+model+for+task+oriented+object+detection) `bib:chen2024taskclip`
- **Robovqa: Multimodal long-horizon reasoning for robotics**. Sermanet, Pierre et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2024. [search only](https://scholar.google.com/scholar?q=Robovqa%3A+Multimodal+long-horizon+reasoning+for+robotics) `bib:sermanet2024robovqa`
- **Reason2Drive: Towards interpretable and chain-based reasoning for autonomous driving**. Nie, Ming et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [[DOI]](https://doi.org/10.1007/978-3-031-73347-5_17) `bib:nie2024reason2drive`
- **Physically grounded vision-language models for robotic manipulation**. Gao, Jensen et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2024. [search only](https://scholar.google.com/scholar?q=Physically+grounded+vision-language+models+for+robotic+manipulation) `bib:gao2024physically`
- **MapLM: A real-world large-scale vision-language benchmark for map and traffic scene understanding**. Cao, Xu et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=MapLM%3A+A+real-world+large-scale+vision-language+benchmark+for+map+and+traffic+scene+understanding) `bib:cao2024maplm`
- **Making large language models better planners with reasoning-decision alignment**. Huang, Zhijian et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Making+large+language+models+better+planners+with+reasoning-decision+alignment) `bib:huang2024making`
- **LamPilot: An open benchmark dataset for autonomous driving with language model programs**. Ma, Yunsheng et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=LamPilot%3A+An+open+benchmark+dataset+for+autonomous+driving+with+language+model+programs) `bib:ma2024lampilot`
- **LMDrive: Closed-loop end-to-end driving with large language models**. Shao, Hao et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=LMDrive%3A+Closed-loop+end-to-end+driving+with+large+language+models) `bib:shao2024lmdrive`
- **From pixels to graphs: Open-vocabulary scene graph generation with vision-language models**. Li, Rongjie et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=From+pixels+to+graphs%3A+Open-vocabulary+scene+graph+generation+with+vision-language+models) `bib:li2024pixels`
- **DriveLM: Driving with graph visual question answering**. Sima, Chonghao et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=DriveLM%3A+Driving+with+graph+visual+question+answering) `bib:sima2024drivelm`
- **DriveGPT4: Interpretable end-to-end autonomous driving via large language model**. Xu, Zhenhua et al., IEEE Robot. Autom. Lett., 2024. [[DOI]](https://doi.org/10.1109/LRA.2024.3440097) `bib:xu2024drivegpt4`
- **Dream2real: Zero-shot 3d object rearrangement with vision-language models**. Kapelyukh, Ivan et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2024. [search only](https://scholar.google.com/scholar?q=Dream2real%3A+Zero-shot+3d+object+rearrangement+with+vision-language+models) `bib:kapelyukh2024dream2real`
- **Dolphins: Multimodal language model for driving**. Ma, Yingzi et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Dolphins%3A+Multimodal+language+model+for+driving) `bib:ma2024dolphins`
- **Brave: Broadening the visual encoding of vision-language models**. Kar, Oguzhan Fatih et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Brave%3A+Broadening+the+visual+encoding+of+vision-language+models) `bib:kar2024brave`
- **Reasonnet: End-to-end driving with temporal and global reasoning**. Shao, Hao et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Reasonnet%3A+End-to-end+driving+with+temporal+and+global+reasoning) `bib:shao2023reasonnet`
- **GPT-Driver: Learning to Drive with GPT**. Mao, Jiageng et al., misc, 2023. [[arXiv]](https://arxiv.org/abs/2310.01415) `bib:mao2023gpt`
- **DreamWalker: Mental planning for continuous vision-language navigation**. Wang, Hanqing et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=DreamWalker%3A+Mental+planning+for+continuous+vision-language+navigation) `bib:wang2023dreamwalker`

## World Models, Rollout, and Generative Simulation

- **Drive-JEPA: Video JEPA meets multimodal trajectory distillation for end-to-end driving**. Wang, Linhan et al., misc, 2026. [[arXiv]](https://arxiv.org/abs/2601.22032) `bib:wang2026drive`
- **World4Drive: End-to-end autonomous driving via intention-aware physical latent world model**. Zheng, Yupeng et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=World4Drive%3A+End-to-end+autonomous+driving+via+intention-aware+physical+latent+world+model) `bib:zheng2025world4drive`
- **Muvo: A multimodal generative world model for autonomous driving with geometric representations**. Bogdoll, Daniel et al., Proc. IEEE Intell. Vehicles Symp. (IV), 2025. [search only](https://scholar.google.com/scholar?q=Muvo%3A+A+multimodal+generative+world+model+for+autonomous+driving+with+geometric+representations) `bib:bogdoll2025muvo`
- **Gaia-2: A controllable multi-view generative world model for autonomous driving**. Russell, Lloyd et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2503.20523) `bib:russell2025gaia`
- **Epona: Autoregressive diffusion world model for autonomous driving**. Zhang, Kaiwen et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=Epona%3A+Autoregressive+diffusion+world+model+for+autonomous+driving) `bib:zhang2025epona`
- **Enhancing end-to-end autonomous driving with latent world model**. Li, Yingyan et al., Proc. Int. Conf. Learn. Represent. (ICLR), 2025. [search only](https://scholar.google.com/scholar?q=Enhancing+end-to-end+autonomous+driving+with+latent+world+model) `bib:li2024enhancing`
- **End-to-End Driving with Online Trajectory Evaluation via BEV World Model**. Li, Yingyan et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=End-to-End+Driving+with+Online+Trajectory+Evaluation+via+BEV+World+Model) `bib:li2025end`
- **DriveDreamer4D: World models are effective data machines for 4D driving scene representation**. Zhao, Guosheng et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [search only](https://scholar.google.com/scholar?q=DriveDreamer4D%3A+World+models+are+effective+data+machines+for+4D+driving+scene+representation) `bib:zhao2025drivedreamer4d`
- **DriveArena: A closed-loop generative simulation platform for autonomous driving**. Yang, Xuemeng et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=DriveArena%3A+A+closed-loop+generative+simulation+platform+for+autonomous+driving) `bib:yang2025drivearena`
- **Cardreamer: Open-source learning platform for world model based autonomous driving**. Gao, Dechen et al., IEEE Internet Things J., 2025. [[DOI]](https://doi.org/10.1109/JIOT.2024.3479088) `bib:gao2024cardreamer`
- **Artemis: Autoregressive end-to-end trajectory planning with mixture of experts for autonomous driving**. Feng, Renju et al., IEEE Robot. Autom. Lett., 2025. [search only](https://scholar.google.com/scholar?q=Artemis%3A+Autoregressive+end-to-end+trajectory+planning+with+mixture+of+experts+for+autonomous+driving) `bib:feng2025artemis`
- **SparseOcc: Rethinking sparse latent representation for vision-based semantic occupancy prediction**. Tang, Pin et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=SparseOcc%3A+Rethinking+sparse+latent+representation+for+vision-based+semantic+occupancy+prediction) `bib:tang2024sparseocc`
- **OccWorld: Learning a 3D occupancy world model for autonomous driving**. Zheng, Wenzhao et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=OccWorld%3A+Learning+a+3D+occupancy+world+model+for+autonomous+driving) `bib:zheng2024occworld`
- **Neural volumetric world models for autonomous driving**. Huang, Zanming et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Neural+volumetric+world+models+for+autonomous+driving) `bib:huang2024neural`
- **Genad: Generative end-to-end autonomous driving**. Zheng, Wenzhao et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Genad%3A+Generative+end-to-end+autonomous+driving) `bib:zheng2024genad`
- **Enhance sample efficiency and robustness of end-to-end urban autonomous driving via semantic masked world model**. Gao, Zeyu et al., IEEE Trans. Intell. Transp. Syst., 2024. [search only](https://scholar.google.com/scholar?q=Enhance+sample+efficiency+and+robustness+of+end-to-end+urban+autonomous+driving+via+semantic+masked+world+model) `bib:gao2024enhance`
- **Driving into the future: Multiview visual forecasting and planning with world model for autonomous driving**. Wang, Yuqi et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Driving+into+the+future%3A+Multiview+visual+forecasting+and+planning+with+world+model+for+autonomous+driving) `bib:wang2024driving`
- **DriveWorld: 4D pre-trained scene understanding via world models for autonomous driving**. Min, Chen et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=DriveWorld%3A+4D+pre-trained+scene+understanding+via+world+models+for+autonomous+driving) `bib:min2024driveworld`
- **DriveDreamer: Towards real-world-drive world models for autonomous driving**. Wang, Xiaofeng et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=DriveDreamer%3A+Towards+real-world-drive+world+models+for+autonomous+driving) `bib:wang2024drivedreamer`
- **Dream to adapt: Meta reinforcement learning by latent context imagination and MDP imagination**. Wen, Lu et al., IEEE Robot. Autom. Lett., 2024. [search only](https://scholar.google.com/scholar?q=Dream+to+adapt%3A+Meta+reinforcement+learning+by+latent+context+imagination+and+MDP+imagination) `bib:wen2024dream`
- **Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion**. Zhang, Lunjun et al., Proc. Int. Conf. Learn. Represent. (ICLR), 2024. [search only](https://scholar.google.com/scholar?q=Copilot4D%3A+Learning+Unsupervised+World+Models+for+Autonomous+Driving+via+Discrete+Diffusion) `bib:zhang2024copilot4d`
- **TrafficBots: Towards World Models for Autonomous Driving Simulation and Motion Prediction**. Zhang, Zhejun et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2023. [[DOI]](https://doi.org/10.1109/ICRA48891.2023.10161243) `bib:zhang2023trafficbots`
- **Persistent nature: A generative model of unbounded 3d worlds**. Chai, Lucy et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Persistent+nature%3A+A+generative+model+of+unbounded+3d+worlds) `bib:chai2023persistent`
- **Gaia-1: A generative world model for autonomous driving**. Hu, Anthony et al., misc, 2023. [[arXiv]](https://arxiv.org/abs/2309.17080) `bib:hu2023gaia`
- **Future video frame prediction based on generative motion-assistant discriminative network**. Li, Chenming et al., Appl. Soft Comput., 2023. [search only](https://scholar.google.com/scholar?q=Future+video+frame+prediction+based+on+generative+motion-assistant+discriminative+network) `bib:li2023future`
- **World model learning from demonstrations with active inference: application to driving behavior**. Wei, Ran et al., Int. Workshop Active Inference, 2022. [search only](https://scholar.google.com/scholar?q=World+model+learning+from+demonstrations+with+active+inference%3A+application+to+driving+behavior) `bib:wei2022world`
- **Navdreams: Towards camera-only rl navigation among humans**. Dugas, Daniel et al., Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), 2022. [search only](https://scholar.google.com/scholar?q=Navdreams%3A+Towards+camera-only+rl+navigation+among+humans) `bib:dugas2022navdreams`
- **Learning a world model with multitimescale memory augmentation**. Cai, Wenzhe et al., IEEE Trans. Neural Netw. Learn. Syst., 2022. [search only](https://scholar.google.com/scholar?q=Learning+a+world+model+with+multitimescale+memory+augmentation) `bib:cai2022learning`
- **Dynamic-horizon model-based value estimation with latent imagination**. Wang, Junjie et al., IEEE Trans. Neural Netw. Learn. Syst., 2022. [search only](https://scholar.google.com/scholar?q=Dynamic-horizon+model-based+value+estimation+with+latent+imagination) `bib:wang2022dynamic`
- **Dreamingv2: Reinforcement learning with discrete world models without reconstruction**. Okada, Masashi et al., Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), 2022. [search only](https://scholar.google.com/scholar?q=Dreamingv2%3A+Reinforcement+learning+with+discrete+world+models+without+reconstruction) `bib:okada2022dreamingv2`
- **Pathdreamer: A world model for indoor navigation**. Koh, Jing Yu et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021. [search only](https://scholar.google.com/scholar?q=Pathdreamer%3A+A+world+model+for+indoor+navigation) `bib:koh2021pathdreamer`
- **MAMBPO: Sample-efficient multi-robot reinforcement learning using learned world models**. Willemsen, Daniel et al., Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), 2021. [search only](https://scholar.google.com/scholar?q=MAMBPO%3A+Sample-efficient+multi-robot+reinforcement+learning+using+learned+world+models) `bib:willemsen2021mambpo`

## Planning-Oriented Evaluation and Benchmarks

- **Pseudo-Simulation for Autonomous Driving**. Cao, Wei et al., Proc. Conf. Robot Learn. (CoRL), 2025. [search only](https://scholar.google.com/scholar?q=Pseudo-Simulation+for+Autonomous+Driving) `bib:Cao2025CORL`
- **NAVSIM: Data-driven non-reactive autonomous vehicle simulation and benchmarking**. Dauner, Daniel et al., Proc. Adv. Neural Inf. Process. Syst., 2024. [search only](https://scholar.google.com/scholar?q=NAVSIM%3A+Data-driven+non-reactive+autonomous+vehicle+simulation+and+benchmarking) `bib:dauner2024navsim`
- **Cam4DOcc: Benchmark for camera-only 4D occupancy forecasting in autonomous driving applications**. Ma, Junyi et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Cam4DOcc%3A+Benchmark+for+camera-only+4D+occupancy+forecasting+in+autonomous+driving+applications) `bib:ma2024cam4docc`
- **Bench2Drive: Towards multi-ability benchmarking of closed-loop end-to-end autonomous driving**. Jia, Xiaosong et al., Proc. Adv. Neural Inf. Process. Syst., 2024. [search only](https://scholar.google.com/scholar?q=Bench2Drive%3A+Towards+multi-ability+benchmarking+of+closed-loop+end-to-end+autonomous+driving) `bib:jia2024bench2drive`
- **Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research**. Gulino, Cole et al., Proc. Adv. Neural Inf. Process. Syst., 2023. [search only](https://scholar.google.com/scholar?q=Waymax%3A+An+Accelerated%2C+Data-Driven+Simulator+for+Large-Scale+Autonomous+Driving+Research) `bib:gulino2023waymax`
- **ScenarioNet: Open-Source Platform for Large-Scale Traffic Scenario Simulation and Modeling**. Li, Quanyi et al., Proc. Adv. Neural Inf. Process. Syst., 2023. [search only](https://scholar.google.com/scholar?q=ScenarioNet%3A+Open-Source+Platform+for+Large-Scale+Traffic+Scenario+Simulation+and+Modeling) `bib:li2023scenarionet`
- **MixSim: A Hierarchical Framework for Mixed Reality Traffic Simulation**. Suo, Simon et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=MixSim%3A+A+Hierarchical+Framework+for+Mixed+Reality+Traffic+Simulation) `bib:suo2023mixsim`
- **Argoverse 2: Next generation datasets for self-driving perception and forecasting**. Wilson, Benjamin et al., misc, 2023. [[arXiv]](https://arxiv.org/abs/2301.00493) `bib:wilson2023argoverse2`
- **DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection**. Yu, Haibao et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022. [search only](https://scholar.google.com/scholar?q=DAIR-V2X%3A+A+Large-Scale+Dataset+for+Vehicle-Infrastructure+Cooperative+3D+Object+Detection) `bib:yu2022dairv2x`
- **nuPlan: A closed-loop ML-based planning benchmark for autonomous vehicles**. Caesar, Holger et al., misc, 2021. [[arXiv]](https://arxiv.org/abs/2106.11810) `bib:caesar2021nuplan`
- **Large scale interactive motion forecasting for autonomous driving: The Waymo open motion dataset**. Ettinger, Scott et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021. [search only](https://scholar.google.com/scholar?q=Large+scale+interactive+motion+forecasting+for+autonomous+driving%3A+The+Waymo+open+motion+dataset) `bib:ettinger2021womd`
- **nuScenes: A multimodal dataset for autonomous driving**. Caesar, Holger et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020. [search only](https://scholar.google.com/scholar?q=nuScenes%3A+A+multimodal+dataset+for+autonomous+driving) `bib:caesar2020nuscenes`
- **BDD100K: A Diverse Driving Dataset for Heterogeneous Multitask Learning**. Yu, Fisher et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020. [[DOI]](https://doi.org/10.1109/CVPR42600.2020.00271) `bib:yu2020bdd100k`
- **CARLA: An open urban driving simulator**. Dosovitskiy, Alexey et al., Proc. Conf. Robot Learn. (CoRL), 2017. [search only](https://scholar.google.com/scholar?q=CARLA%3A+An+open+urban+driving+simulator) `bib:dosovitskiy2017carla`

## BEV, Occupancy, and Perception

- **SimpleVSF: VLM-scoring fusion for trajectory prediction of end-to-end autonomous driving**. Zheng, Peiru et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2510.17191) `bib:zheng2025simplevsf`
- **Efficient and robust multi-camera 3D object detection in bird-eye-view**. Wang, Yuanlong et al., Image Vis. Comput., 2025. [search only](https://scholar.google.com/scholar?q=Efficient+and+robust+multi-camera+3D+object+detection+in+bird-eye-view) `bib:wang2025efficient`
- **DiffusionDriveV2: Reinforcement learning-constrained truncated diffusion modeling in end-to-end autonomous driving**. Jialv Zou et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2512.07745) `bib:zou2025diffusiondrivev2reinforcementlearningconstrainedtruncated`
- **DiffusionDriveV2: Reinforcement learning-constrained truncated diffusion modeling in end-to-end autonomous driving**. Zou, Jialv et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2512.07745) `bib:zou2025diffusiondrivev2`
- **DiffusionDrive: Truncated diffusion model for end-to-end autonomous driving**. Bencheng Liao et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [[DOI]](https://doi.org/10.1109/CVPR52734.2025.01124) `bib:diffusiondrive`
- **DIVER: Reinforced diffusion breaks imitation bottlenecks in end-to-end autonomous driving**. Song, Ziying et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2507.04049) `bib:song2025diver`
- **BEVFormer: learning bird's-eye-view representation from LiDAR-camera via spatiotemporal transformers**. Li, Zhiqi et al., IEEE Trans. Pattern Anal. Mach. Intell., 2025. [[DOI]](https://doi.org/10.1109/TPAMI.2024.3515454) `bib:li2024bevformer`
- **Uno: Unsupervised occupancy fields for perception and forecasting**. Agro, Ben et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Uno%3A+Unsupervised+occupancy+fields+for+perception+and+forecasting) `bib:agro2024uno`
- **Unibev: Multi-modal 3d object detection with uniform bev encoders for robustness against missing sensor modalities**. Wang, Shiming et al., Proc. IEEE Intell. Vehicles Symp. (IV), 2024. [search only](https://scholar.google.com/scholar?q=Unibev%3A+Multi-modal+3d+object+detection+with+uniform+bev+encoders+for+robustness+against+missing+sensor+modalities) `bib:wang2024unibev`
- **TS-BEV: BEV object detection algorithm based on temporal-spatial feature fusion**. Dong, Xinlong et al., Displays, 2024. [search only](https://scholar.google.com/scholar?q=TS-BEV%3A+BEV+object+detection+algorithm+based+on+temporal-spatial+feature+fusion) `bib:dong2024ts`
- **StreamingFlow: Streaming occupancy forecasting with asynchronous multi-modal data streams via neural ordinary differential equation**. Shi, Yining et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=StreamingFlow%3A+Streaming+occupancy+forecasting+with+asynchronous+multi-modal+data+streams+via+neural+ordinary+differential+equation) `bib:shi2024streamingflow`
- **PanoOcc: Unified occupancy representation for camera-based 3D panoptic segmentation**. Wang, Yuqi et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=PanoOcc%3A+Unified+occupancy+representation+for+camera-based+3D+panoptic+segmentation) `bib:wang2024panoocc`
- **Occfeat: Self-supervised occupancy feature prediction for pretraining bev segmentation networks**. Sirko-Galouchenko, Sophia et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Occfeat%3A+Self-supervised+occupancy+feature+prediction+for+pretraining+bev+segmentation+networks) `bib:sirko2024occfeat`
- **MMAF-Net: Multi-view multi-stage adaptive fusion for multi-sensor 3D object detection**. Zhang, Wensheng et al., Expert Syst. Appl., 2024. [search only](https://scholar.google.com/scholar?q=MMAF-Net%3A+Multi-view+multi-stage+adaptive+fusion+for+multi-sensor+3D+object+detection) `bib:zhang2024mmaf`
- **ICOP: Image-based cooperative perception for end-to-end autonomous driving**. Li, Lantao et al., Proc. IEEE Intell. Vehicles Symp. (IV), 2024. [search only](https://scholar.google.com/scholar?q=ICOP%3A+Image-based+cooperative+perception+for+end-to-end+autonomous+driving) `bib:li2024icop`
- **CL-fusionBEV: 3D object detection method with camera-LiDAR fusion in bird's eye view**. Shi, Peicheng et al., Complex Intell. Syst., 2024. [search only](https://scholar.google.com/scholar?q=CL-fusionBEV%3A+3D+object+detection+method+with+camera-LiDAR+fusion+in+bird%27s+eye+view) `bib:shi2024cl`
- **BEVoxSeg: BEV-Voxel Representation for Fast and Accurate Camera-Based 3D Segmentation**. Liu, Haiyi et al., Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), 2024. [search only](https://scholar.google.com/scholar?q=BEVoxSeg%3A+BEV-Voxel+Representation+for+Fast+and+Accurate+Camera-Based+3D+Segmentation) `bib:liu2024bevoxseg`
- **BEVRefiner: Improving 3D object detection in bird's-eye-view via dual refinement**. Wang, Binglu et al., IEEE Trans. Intell. Transp. Syst., 2024. [[DOI]](https://doi.org/10.1109/TITS.2024.3394550) `bib:wang2024bevrefiner`
- **Understanding the Robustness of 3D Object Detection With Bird's-Eye-View Representations in Autonomous Driving**. Zhu, Zijian et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Understanding+the+Robustness+of+3D+Object+Detection+With+Bird%27s-Eye-View+Representations+in+Autonomous+Driving) `bib:zhu2023robustness`
- **Tri-perspective view for vision-based 3D semantic occupancy prediction**. Huang, Yuanhui et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Tri-perspective+view+for+vision-based+3D+semantic+occupancy+prediction) `bib:huang2023tri`
- **TransFuser: Imitation With Transformer-Based Sensor Fusion for Autonomous Driving**. Chitta, Kashyap et al., IEEE Trans. Pattern Anal. Mach. Intell., 2023. [search only](https://scholar.google.com/scholar?q=TransFuser%3A+Imitation+With+Transformer-Based+Sensor+Fusion+for+Autonomous+Driving) `bib:chitta2023transfuser`
- **Towards Viewpoint Robustness in Bird's Eye View Segmentation**. Klinghoffer, Tzofi et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=Towards+Viewpoint+Robustness+in+Bird%27s+Eye+View+Segmentation) `bib:klinghoffer2023viewpoint`
- **Temporal enhanced training of multi-view 3d object detector via historical object prediction**. Zong, Zhuofan et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=Temporal+enhanced+training+of+multi-view+3d+object+detector+via+historical+object+prediction) `bib:zong2023temporal`
- **SurroundOcc: Multi-camera 3D occupancy prediction for autonomous driving**. Wei, Yi et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=SurroundOcc%3A+Multi-camera+3D+occupancy+prediction+for+autonomous+driving) `bib:wei2023surroundocc`
- **Occformer: Dual-path transformer for vision-based 3d semantic occupancy prediction**. Zhang, Yunpeng et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=Occformer%3A+Dual-path+transformer+for+vision-based+3d+semantic+occupancy+prediction) `bib:zhang2023occformer`
- **Monocular road scene bird's eye view prediction via big kernel-size encoder and spatial-channel transform module**. Rao, Zhongyu et al., IEEE Trans. Intell. Transp. Syst., 2023. [search only](https://scholar.google.com/scholar?q=Monocular+road+scene+bird%27s+eye+view+prediction+via+big+kernel-size+encoder+and+spatial-channel+transform+module) `bib:rao2023monocular`
- **Cooperative perception with V2V communication for autonomous vehicles**. Ngo, Hieu et al., IEEE Trans. Veh. Technol., 2023. [search only](https://scholar.google.com/scholar?q=Cooperative+perception+with+V2V+communication+for+autonomous+vehicles) `bib:ngo2023cooperative`
- **CenterTube: Tracking multiple 3D objects with 4D tubelets in dynamic point clouds**. Liu, Hao et al., IEEE Trans. Multimedia, 2023. [search only](https://scholar.google.com/scholar?q=CenterTube%3A+Tracking+multiple+3D+objects+with+4D+tubelets+in+dynamic+point+clouds) `bib:liu2023centertube`
- **BEVFusion: Multi-task multi-sensor fusion with unified bird's-eye-view representation**. Liu, Zhijian et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2023. [[DOI]](https://doi.org/10.1109/ICRA48891.2023.10160968) `bib:liu2024bevfusionmultitaskmultisensorfusion`
- **BEVFormer V2: Adapting modern image backbones to bird's-eye-view recognition via perspective supervision**. Yang, Chenyu et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=BEVFormer+V2%3A+Adapting+modern+image+backbones+to+bird%27s-eye-view+recognition+via+perspective+supervision) `bib:yang2023bevformer`
- **Mutr3d: A multi-camera tracking framework via 3d-to-2d queries**. Zhang, Tianyuan et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022. [search only](https://scholar.google.com/scholar?q=Mutr3d%3A+A+multi-camera+tracking+framework+via+3d-to-2d+queries) `bib:zhang2022mutr3d`
- **BEVerse: Unified perception and prediction in birds-eye-view for vision-centric autonomous driving**. Zhang, Yunpeng et al., misc, 2022. [[arXiv]](https://arxiv.org/abs/2205.09743) `bib:zhang2022beverseunifiedperceptionprediction`
- **Multi-modal fusion transformer for end-to-end autonomous driving**. Prakash, Aditya et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2021. [search only](https://scholar.google.com/scholar?q=Multi-modal+fusion+transformer+for+end-to-end+autonomous+driving) `bib:prakash2021multi`
- **Fiery: Future instance prediction in bird's-eye view from surround monocular cameras**. Hu, Anthony et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021. [search only](https://scholar.google.com/scholar?q=Fiery%3A+Future+instance+prediction+in+bird%27s-eye+view+from+surround+monocular+cameras) `bib:hu2021fiery`
- **Enabling spatio-temporal aggregation in birds-eye-view vehicle estimation**. Saha, Avishkar et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2021. [search only](https://scholar.google.com/scholar?q=Enabling+spatio-temporal+aggregation+in+birds-eye-view+vehicle+estimation) `bib:saha2021enabling`
- **Driving among flatmobiles: Bird-eye-view occupancy grids from a monocular camera for holistic trajectory planning**. Loukkal, Abdelhak et al., Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. (WACV), 2021. [search only](https://scholar.google.com/scholar?q=Driving+among+flatmobiles%3A+Bird-eye-view+occupancy+grids+from+a+monocular+camera+for+holistic+trajectory+planning) `bib:loukkal2021driving`
- **BEVDetNet: Bird's eye view LiDAR point cloud based real-time 3D object detection for autonomous driving**. Mohapatra, Sambit et al., Proc. IEEE Intell. Transp. Syst. Conf. (ITSC), 2021. [search only](https://scholar.google.com/scholar?q=BEVDetNet%3A+Bird%27s+eye+view+LiDAR+point+cloud+based+real-time+3D+object+detection+for+autonomous+driving) `bib:mohapatra2021bevdetnet`
- **Train in Germany, Test in the USA: Making 3D Object Detectors Generalize**. Wang, Yan et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020. [[DOI]](https://doi.org/10.1109/CVPR42600.2020.01173) `bib:wang2020germanyusa`
- **Autonomous vehicle perception: The technology of today and tomorrow**. Van Brummelen, Jessica et al., Transportation Research Part C: Emerging Technologies, 2018. [[DOI]](https://doi.org/10.1016/j.trc.2018.02.012) `bib:vanbrummelen2018autonomous`

## Trajectory Prediction and End-to-End Planning

- **Reinforced refinement with self-aware expansion for end-to-end autonomous driving**. Liu, Haochen et al., IEEE Trans. Pattern Anal. Mach. Intell., 2026. [[DOI]](https://doi.org/10.1109/TPAMI.2026.3653866) `bib:liu2026reinforced`
- **DriveSuprim: Towards precise trajectory selection for end-to-end planning**. Yao, Wenhao et al., Proc. AAAI Conf. Artif. Intell., 2026. [[DOI]](https://doi.org/10.1609/AAAI.V40I14.38178) `bib:yao2025drivesuprim`
- **TransDiffuser: Diverse trajectory generation with decorrelated multi-modal representation for end-to-end autonomous driving**. Jiang, Xuefeng et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2505.09315) `bib:jiang2025transdiffuser`
- **ResAD: Normalized Residual Trajectory Modeling for End-to-End Autonomous Driving**. Zheng, Zhiyu et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2510.08562) `bib:zheng2025resad`
- **Hydra-NeXt: Robust Closed-Loop Driving with Open-Loop Training**. Li, Zhenxin et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=Hydra-NeXt%3A+Robust+Closed-Loop+Driving+with+Open-Loop+Training) `bib:li2025hydra_next`
- **Hydra-MDP++: Advancing end-to-end driving via expert-guided hydra-distillation**. Li, Kailin et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2503.12820) `bib:li2025hydra`
- **GoalFlow: Goal-driven flow matching for multimodal trajectories generation in end-to-end autonomous driving**. Xing, Zebin et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2025. [search only](https://scholar.google.com/scholar?q=GoalFlow%3A+Goal-driven+flow+matching+for+multimodal+trajectories+generation+in+end-to-end+autonomous+driving) `bib:xing2025goalflow`
- **DriveDPO: Policy learning via safety DPO for end-to-end autonomous driving**. Shang, Shuyao et al., Proc. Adv. Neural Inf. Process. Syst., 2025. [search only](https://scholar.google.com/scholar?q=DriveDPO%3A+Policy+learning+via+safety+DPO+for+end-to-end+autonomous+driving) `bib:shang2025drivedpo`
- **Distilldrive: End-to-end multi-mode autonomous driving distillation by isomorphic hetero-source planning model**. Yu, Rui et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2025. [search only](https://scholar.google.com/scholar?q=Distilldrive%3A+End-to-end+multi-mode+autonomous+driving+distillation+by+isomorphic+hetero-source+planning+model) `bib:yu2025distilldrive`
- **Centaur: Robust end-to-end autonomous driving with test-time training**. Sima, Chonghao et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2503.11650) `bib:sima2025centaur`
- **SMART: Scalable Multi-Agent Real-Time Motion Generation via Next-Token Prediction**. Wu, Wei et al., Proc. Adv. Neural Inf. Process. Syst., 2024. [search only](https://scholar.google.com/scholar?q=SMART%3A+Scalable+Multi-Agent+Real-Time+Motion+Generation+via+Next-Token+Prediction) `bib:wu2024smart`
- **Prototypical context-aware dynamics for generalization in visual control with model-based reinforcement learning**. Wang, Junjie et al., IEEE Trans. Ind. Informat., 2024. [search only](https://scholar.google.com/scholar?q=Prototypical+context-aware+dynamics+for+generalization+in+visual+control+with+model-based+reinforcement+learning) `bib:wang2024prototypical`
- **Motion Forecasting in Continuous Driving**. Song, Nan et al., Proc. Adv. Neural Inf. Process. Syst., 2024. [search only](https://scholar.google.com/scholar?q=Motion+Forecasting+in+Continuous+Driving) `bib:song2024continuous`
- **MTR++: Multi-Agent Motion Prediction With Symmetric Scene Modeling and Guided Intention Querying**. Shi, Shaoshuai et al., IEEE Trans. Pattern Anal. Mach. Intell., 2024. [[DOI]](https://doi.org/10.1109/TPAMI.2024.3352811) `bib:shi2024mtrpp`
- **Evolutionary end-to-end autonomous driving model with continuous-time neural networks**. Du, Jiatong et al., IEEE/ASME Trans. Mechatronics, 2024. [search only](https://scholar.google.com/scholar?q=Evolutionary+end-to-end+autonomous+driving+model+with+continuous-time+neural+networks) `bib:du2024evolutionary`
- **Drive anywhere: Generalizable end-to-end autonomous driving with multi-modal foundation models**. Wang, Tsun-Hsuan et al., Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2024. [search only](https://scholar.google.com/scholar?q=Drive+anywhere%3A+Generalizable+end-to-end+autonomous+driving+with+multi-modal+foundation+models) `bib:wang2024drive`
- **Drama: An efficient end-to-end motion planner for autonomous driving with mamba**. Yuan, Chengran et al., misc, 2024. [[arXiv]](https://arxiv.org/abs/2408.03601) `bib:yuan2024drama`
- **Data-efficient model-based reinforcement learning with trajectory discrimination**. Qu, Tuo et al., Complex Intell. Syst., 2024. [search only](https://scholar.google.com/scholar?q=Data-efficient+model-based+reinforcement+learning+with+trajectory+discrimination) `bib:qu2024data`
- **Rethinking the open-loop evaluation of end-to-end autonomous driving in nuScenes**. Zhai, Jiang-Tian et al., misc, 2023. [[arXiv]](https://arxiv.org/abs/2305.10430) `bib:zhai2023rethinking`
- **Query-Centric Trajectory Prediction**. Zhou, Zikang et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [[DOI]](https://doi.org/10.1109/CVPR52729.2023.01713) `bib:zhou2023query`
- **QCNeXt: A next-generation framework for joint multi-agent trajectory prediction**. Zhou, Zikang et al., misc, 2023. [[arXiv]](https://arxiv.org/abs/2306.10508) `bib:zhou2023qcnext`
- **Planning-oriented autonomous driving**. Hu, Yihan et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Planning-oriented+autonomous+driving) `bib:hu2023planning`
- **Parting with Misconceptions about Learning-based Vehicle Motion Planning**. Dauner, Daniel et al., Proc. Conf. Robot Learn. (CoRL), 2023. [search only](https://scholar.google.com/scholar?q=Parting+with+Misconceptions+about+Learning-based+Vehicle+Motion+Planning) `bib:chitta2023parting`
- **ST-P3: End-to-End Vision-Based Autonomous Driving via Spatial-Temporal Feature Learning**. Hu, Shengchao et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2022. [[DOI]](https://doi.org/10.1007/978-3-031-19839-7_31) `bib:hu2022st`
- **HiVT: Hierarchical vector transformer for multi-agent motion prediction**. Zhou, Junyu et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022. [search only](https://scholar.google.com/scholar?q=HiVT%3A+Hierarchical+vector+transformer+for+multi-agent+motion+prediction) `bib:zhou2022hivt`
- **Continuous control of autonomous vehicles using plan-assisted deep reinforcement learning**. Dwivedi, Tanay et al., Proc. Int. Conf. Control Autom. Syst. (ICCAS), 2022. [search only](https://scholar.google.com/scholar?q=Continuous+control+of+autonomous+vehicles+using+plan-assisted+deep+reinforcement+learning) `bib:dwivedi2022continuous`
- **Multi-task learning with attention for end-to-end autonomous driving**. Ishihara, Keishi et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2021. [search only](https://scholar.google.com/scholar?q=Multi-task+learning+with+attention+for+end-to-end+autonomous+driving) `bib:ishihara2021multi`

## Other Relevant Papers

- **Driving on Registers**. Kirby, Ellington et al., misc, 2026. [[arXiv]](https://arxiv.org/abs/2601.05083) `bib:kirby2026driving`
- **Predictive Reachability for Embodiment Selection in Mobile Manipulation Behaviors**. Feng, Xiaoxu et al., IEEE Robot. Autom. Lett., 2025. [[DOI]](https://doi.org/10.1109/LRA.2025.3539097) `bib:feng2025predictive`
- **Learning Personalized Driving Styles via Reinforcement Learning from Human Feedback**. Li, Derun et al., misc, 2025. [[arXiv]](https://arxiv.org/abs/2503.10434) `bib:li2025learning`
- **VWP: An Efficient DRL-Based Autonomous Driving Model**. Jin, Yan-Liang et al., IEEE Trans. Multimedia, 2024. [[DOI]](https://doi.org/10.1109/TMM.2022.3177942) `bib:jin2022vwp`
- **Para-drive: Parallelized architecture for real-time autonomous driving**. Weng, Xinshuo et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Para-drive%3A+Parallelized+architecture+for+real-time+autonomous+driving) `bib:weng2024drive`
- **Fiptr: A simple yet effective transformer framework for future instance prediction in autonomous driving**. Gui, Xingtai et al., Proc. Eur. Conf. Comput. Vis. (ECCV), 2024. [search only](https://scholar.google.com/scholar?q=Fiptr%3A+A+simple+yet+effective+transformer+framework+for+future+instance+prediction+in+autonomous+driving) `bib:gui2024fiptr`
- **Feedback-guided autonomous driving**. Zhang, Jimuyang et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2024. [search only](https://scholar.google.com/scholar?q=Feedback-guided+autonomous+driving) `bib:zhang2024feedback`
- **Assessing quality metrics for neural reality gap input mitigation in autonomous driving testing**. Lambertenghi, Stefano Carlo et al., Proc. IEEE Conf. Softw. Testing Verif. Validation (ICST), 2024. [search only](https://scholar.google.com/scholar?q=Assessing+quality+metrics+for+neural+reality+gap+input+mitigation+in+autonomous+driving+testing) `bib:lambertenghi2024assessing`
- **VAD: Vectorized scene representation for efficient autonomous driving**. Jiang, Bo et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2023. [search only](https://scholar.google.com/scholar?q=VAD%3A+Vectorized+scene+representation+for+efficient+autonomous+driving) `bib:jiang2023vad`
- **Model-Based Reinforcement Learning With Isolated Imaginations**. Pan, Minting et al., IEEE Trans. Pattern Anal. Mach. Intell., 2023. [search only](https://scholar.google.com/scholar?q=Model-Based+Reinforcement+Learning+With+Isolated+Imaginations) `bib:pan2023model`
- **Dyna-PPO reinforcement learning with Gaussian process for the continuous action decision-making in autonomous driving**. Wu, Guanlin et al., Appl. Intell., 2023. [search only](https://scholar.google.com/scholar?q=Dyna-PPO+reinforcement+learning+with+Gaussian+process+for+the+continuous+action+decision-making+in+autonomous+driving) `bib:wu2023dyna`
- **Aligning bag of regions for open-vocabulary object detection**. Wu, Size et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2023. [search only](https://scholar.google.com/scholar?q=Aligning+bag+of+regions+for+open-vocabulary+object+detection) `bib:wu2023aligning`
- **ADAPT: Action-aware driving caption transformer**. Jin, Bu et al., Proc. CAAI Int. Conf. Artif. Intell., 2023. [search only](https://scholar.google.com/scholar?q=ADAPT%3A+Action-aware+driving+caption+transformer) `bib:jin2023adapt`
- **Continual predictive learning from videos**. Chen, Geng et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022. [search only](https://scholar.google.com/scholar?q=Continual+predictive+learning+from+videos) `bib:chen2022continual`
- **Vision-based autonomous car racing using deep imitative reinforcement learning**. Cai, Peide et al., IEEE Robot. Autom. Lett., 2021. [search only](https://scholar.google.com/scholar?q=Vision-based+autonomous+car+racing+using+deep+imitative+reinforcement+learning) `bib:cai2021vision`
- **Model-based soft actor-critic**. Chien, Jen-Tzung et al., 2021 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC), 2021. [search only](https://scholar.google.com/scholar?q=Model-based+soft+actor-critic) `bib:chien2021model`
- **Learning to drive from a world on rails**. Chen, Dian et al., Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021. [search only](https://scholar.google.com/scholar?q=Learning+to+drive+from+a+world+on+rails) `bib:chen2021learning`
- **IA-CNN: A generalised interpretable convolutional neural network with attention mechanism**. Zhang, Zhisong et al., Proc. Int. Joint Conf. Neural Netw. (IJCNN), 2021. [search only](https://scholar.google.com/scholar?q=IA-CNN%3A+A+generalised+interpretable+convolutional+neural+network+with+attention+mechanism) `bib:zhang2021ia`
- **VectorNet: Encoding HD maps and agent dynamics from vectorized representation**. Gao, Jiyang et al., Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020. [search only](https://scholar.google.com/scholar?q=VectorNet%3A+Encoding+HD+maps+and+agent+dynamics+from+vectorized+representation) `bib:gao2020vectornet`

<!-- END PAPER_LIST -->

## Repository Structure

```text
.
|-- README.md
|-- paper_list.md
|-- bibliography/
|   `-- references.bib
|-- papers/
|   |-- link_check.tsv
|   |-- papers.tsv
|   `-- README.md
|-- assets/
|   `-- figures/
|-- tools/
|   `-- generate_papers.py
|-- CONTRIBUTING.md
|-- LICENSE
`-- .gitignore
```

## Updating

After editing `bibliography/references.bib`, regenerate the paper table and Markdown list:

```bash
python tools/generate_papers.py
```

To verify direct DOI/arXiv/URL links:

```bash
python tools/verify_links.py
```

When adding `Code`, `Project`, or `Dataset` links, please verify the link against the paper, the authors' official page, the venue page, or an official organization repository before including it.

## Citation

If this reading list helps your work, please cite the original papers directly. A citation entry for the associated survey can be added after the manuscript is publicly available.
