# Graph Report - raw/autopus-adk  (2026-04-14)

## Corpus Check
- Large corpus: 998 files · ~506,032 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 7751 nodes · 9541 edges · 521 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.81)
- Token cost: 12,500 input · 2,800 output

## God Nodes (most connected - your core abstractions)
1. `Adapter` - 36 edges
2. `Adapter` - 28 edges
3. `MCPServer` - 24 edges
4. `Server` - 22 edges
5. `Adapter` - 21 edges
6. `PipelineExecutor` - 19 edges
7. `HookSession` - 18 edges
8. `WorkerLoop` - 17 edges
9. `CmuxAdapter` - 16 edges
10. `samplePipelineRun()` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Double Diamond Design Methodology Skill` --semantically_similar_to--> `Idea Skill (Multi-Provider Debate)`  [INFERRED] [semantically similar]
  raw/autopus-adk/content/skills/double-diamond.md → raw/autopus-adk/content/skills/idea.md
- `ICE Scoring in Idea Skill` --semantically_similar_to--> `ICE Scoring`  [INFERRED] [semantically similar]
  raw/autopus-adk/content/skills/idea.md → raw/autopus-adk/content/skills/brainstorming.md
- `Double Diamond Design Methodology Skill` --semantically_similar_to--> `Brainstorming Skill`  [INFERRED] [semantically similar]
  raw/autopus-adk/content/skills/double-diamond.md → raw/autopus-adk/content/skills/brainstorming.md
- `Profile Injection into Executor Prompts` --references--> `Python Executor Profile`  [INFERRED]
  raw/autopus-adk/content/skills/agent-pipeline.md → raw/autopus-adk/content/profiles/executor/python.md
- `Profile Injection into Executor Prompts` --references--> `Rust Executor Profile`  [INFERRED]
  raw/autopus-adk/content/skills/agent-pipeline.md → raw/autopus-adk/content/profiles/executor/rust.md

## Hyperedges (group relationships)
- **Autopus 7-Phase Multi-Agent Pipeline** — agent_planner, agent_tester, agent_executor, agent_annotator, agent_validator, agent_reviewer, agent_security_auditor [EXTRACTED 0.95]
- **Multi-Model Orchestration Strategy Set** — concept_debate_strategy, concept_consensus_strategy, concept_detach_mode, pkg_orchestra [EXTRACTED 0.90]
- **PRD → Planning → SPEC Document Pipeline** — skill_prd, skill_planning, concept_spec_document [EXTRACTED 0.95]
- **XLOOP Keep/Discard Decision Mechanism** — concept_xloop, concept_circuit_breaker, concept_simplicity_gate [EXTRACTED 0.95]
- **Autopus Branding and Rule Enforcement System** — rule_branding, rule_lore_commit, rule_file_size_limit, rule_subagent_delegation, rule_language_policy [EXTRACTED 0.90]
- **Quality Assurance Pipeline (TDD + Verification + AX Annotation)** — tdd_skill, verification_skill, ax_annotation_skill [INFERRED 0.85]
- **Parallel Agent Execution System** — subagent_dev_skill, worktree_isolation_skill, adaptive_quality_skill [INFERRED 0.88]
- **Pipeline Quality Gate: Validator + Reviewer + Security Auditor** — concept_5phase_pipeline, concept_coverage_85, skill_testing_strategy [INFERRED 0.85]
- **Parallel Executor with Worktree Isolation** — concept_5phase_pipeline, skill_git_worktrees, concept_profile_injection [EXTRACTED 0.95]

## Communities

### Community 0 - "Platform Adapter Layer"
Cohesion: 0.0
Nodes (116): ClaudeAdapter, CodexAdapter, codexResultEvent, featureCounts, FileMapping, GeminiAdapter, geminiResultEvent, HookConfig (+108 more)

### Community 1 - "A2A Heartbeat & Protocol"
Cohesion: 0.01
Nodes (48): Heartbeat, LifecycleManager, mockRecoverer, pollResponse, PollResult, RESTPoller, RESTPollerConfig, TaskLifecycle (+40 more)

### Community 2 - "Completion Detection"
Cohesion: 0.01
Nodes (56): NewCompletionDetector(), NewCompletionDetectorWithConfig(), signalWaitTimeout(), buildInteractiveLaunchCmd(), shellQuote(), launchInteractiveSessions(), pollUntilSessionReady(), RunInteractivePaneOrchestra() (+48 more)

### Community 3 - "Provider Adapter Interfaces"
Cohesion: 0.01
Nodes (80): Artifact, ProviderAdapter, StreamEvent, TaskConfig, TaskResult, NewPaneBackend(), SelectBackend(), BrowserBackend (+72 more)

### Community 4 - "Cost Estimator & CLI Params"
Cohesion: 0.02
Nodes (70): recordParams, Estimator, roundTo6(), TestEstimateCost_BalancedExecutor(), TestEstimateCost_BalancedValidator(), TestEstimateCost_UltraExecutor(), TestEstimatePipelineCost_MultiplePhases(), makePipelineEvent() (+62 more)

### Community 5 - "Auth & PKCE Flow"
Cohesion: 0.02
Nodes (39): deriveChallengeFromVerifier(), extractErrorCode(), PollForToken(), RequestDeviceCode(), tryTokenExchange(), EstimateTokens(), IterationBudget, ShouldCompress() (+31 more)

### Community 6 - "Auth Server & Credentials"
Cohesion: 0.02
Nodes (66): Credentials, newSuccessDeps(), TestAuthenticateServer_BrowserOpenError(), TestAuthenticateServer_DeviceCodeError(), TestAuthenticateServer_PKCEError(), TestAuthenticateServer_PollTimeout(), TestAuthenticateServer_SaveCredentialsError(), TestAuthenticateServer_Success() (+58 more)

### Community 7 - "Project Analyzer"
Cohesion: 0.02
Nodes (28): newArchCmd(), newArchEnforceCmd(), newArchGenerateCmd(), checkLore(), checkLoreFromFile(), hasValidLoreType(), isExperimentBranch(), lastCommitMessage() (+20 more)

### Community 8 - "Pipeline Checkpoint"
Cohesion: 0.02
Nodes (40): SubprocessPipelineConfig, buildPromptBuilder(), checkpointNotFoundErr(), newPipelineCmd(), newPipelineDashboardCmd(), executeParallel(), getCurrentGitHash(), LoadCheckpointIfContinue() (+32 more)

### Community 9 - "A2A Task & Artifact Model"
Cohesion: 0.02
Nodes (105): AgentCard, ApprovalRequestParams, ApprovalResponseParams, Artifact, IterationBudget, JSONRPCError, JSONRPCNotification, JSONRPCRequest (+97 more)

### Community 10 - "Debate Orchestration Engine"
Cohesion: 0.03
Nodes (65): execFunc, buildJudgmentPrompt(), buildRebuttalPrompt(), findOrBuildJudgeConfig(), runDebate(), runRebuttalRound(), CheckDependencies(), darwinInstallCmd() (+57 more)

### Community 11 - "Agent Create & CLI Commands"
Cohesion: 0.03
Nodes (70): newAgentCmd(), newAgentCreateSubCmd(), parseTools(), runAgentCreate(), validateAgentFrontmatter(), agentFrontmatter, agentTemplateData, skillFrontmatter (+62 more)

### Community 12 - "Orchestra CLI & Job Management"
Cohesion: 0.03
Nodes (27): CollectProviderResult, CollectResult, OrchestraFlags, cleanupJobsInDir(), CleanupStaleJobs(), LoadJob(), newOrchestraCleanupCmd(), runOrchestraCleanup() (+19 more)

### Community 13 - "Pipeline Run Config & Strategy"
Cohesion: 0.03
Nodes (45): pipelineRunConfig, strategyValue, Runner, RunnerOptions, RunnerResult, learnHookCoverageGap(), learnHookReviewIssue(), mapFindingSeverity() (+37 more)

### Community 14 - "LSP Client Adapter"
Cohesion: 0.03
Nodes (8): lspClientAdapter, createLSPClient(), newLSPCmd(), newLSPDefinitionCmd(), newLSPDiagnosticsCmd(), newLSPRefsCmd(), newLSPRenameCmd(), newLSPSymbolsCmd()

### Community 15 - "A2A Server & Task Dispatch"
Cohesion: 0.05
Nodes (21): Server, ServerConfig, TaskHandler, jsonRPCError, jsonRPCRequest, jsonRPCResponse, MCPServer, sseClient (+13 more)

### Community 16 - "Codex Adapter"
Cohesion: 0.04
Nodes (29): Adapter, checksum(), logTransformReport(), hookEntry, mergeHookCategories(), mergeHooks(), stampAutopusMarker(), hooksDoc (+21 more)

### Community 17 - "GHERKIN/EARS Parser"
Cohesion: 0.04
Nodes (12): newSpecCmd(), newSpecNewCmd(), newSpecValidateCmd(), buildPromptOpts(), buildReviewProviders(), hasActiveFindings(), mergeProviderNames(), newSpecReviewCmd() (+4 more)

### Community 18 - "Context Collector"
Cohesion: 0.05
Nodes (15): buildIssueTitle(), confirmIssue(), detectGitRepo(), mockRunner, newIssueCmd(), newIssueListCmd(), newIssueReportCmd(), newIssueSearchCmd() (+7 more)

### Community 19 - "Coverage Gap Reviewer"
Cohesion: 0.04
Nodes (8): TestResolveSingleRun_BySpecID(), TestResolveSingleRun_BySpecID_NotFound(), TestResolveSingleRun_LatestRun(), TestResolveTwoRuns_BySpecID(), TestResolveTwoRuns_BySpecID_NotEnough(), TestResolveTwoRuns_Insufficient(), TestResolveTwoRuns_ReturnsMostRecent(), writeTelemetryEvent()

### Community 20 - "E2E Cobra Command Extractor"
Cohesion: 0.08
Nodes (40): cobraCommand, ExtractCobra(), extractFromFile(), isCobraCommand(), scanCobraCommands(), Extract(), extractFuncSignature(), extractModulePath() (+32 more)

### Community 21 - "Monitor & Network Addresses"
Cohesion: 0.05
Nodes (6): TestMonitorSession_Close(), TestMonitorSession_Close_TerminalError(), TestMonitorSession_Close_WithNilTerm(), errorTerminal, failCloseTerminal, mockTerminal

### Community 22 - "PID Lock"
Cohesion: 0.07
Nodes (19): Lock, readPIDFromFile(), itoa(), TestAcquire_AlreadyHeld_Error(), addWorkerSubcommands(), installDaemon(), isDaemonInstalled(), newWorkerCostCmd() (+11 more)

### Community 23 - "Context7 Client"
Cohesion: 0.05
Nodes (7): EntityBrief, GraphContext, KnowledgeSearcher, searchRequest, searchResponse, SearchResult, HashLine

### Community 24 - "Gemini Adapter"
Cohesion: 0.07
Nodes (6): Adapter, logTransformReport(), replaceMarkerSection(), mergeSettingsMaps(), mergeUnique(), toStringSlice()

### Community 25 - "Mock Adapter"
Cohesion: 0.06
Nodes (9): mockAdapter, stubAdapter, TestByCategory(), TestGeneratePromptText_Content(), TestLoad_ValidYAML(), TestRegistry_DetectAll(), TestRegistry_RegisterAndGet(), TestRegistryRegisterAndGet() (+1 more)

### Community 26 - "CLI Extra Commands"
Cohesion: 0.06
Nodes (0): 

### Community 27 - "A2A Mock Backend"
Cohesion: 0.17
Nodes (28): mockBackend, newMockBackend(), newTestServer(), parseResponse(), TestMCPServer_Initialize(), TestMCPServer_InitializedNotification_IsIgnored(), TestMCPServer_Ping(), TestMCPServer_ResourcesList() (+20 more)

### Community 28 - "Banner & UI Display"
Cohesion: 0.08
Nodes (16): CollectContext(), detectPlatform(), lastNLines(), readConfig(), readTelemetry(), hashBytes(), hashProjectStructure(), hashString() (+8 more)

### Community 29 - "Loop Coverage Tests"
Cohesion: 0.07
Nodes (15): itoa(), TestCleanupPolicy_FileExists(), Workspace, WorkspaceAgent, nopWriteCloser, WorkspaceConfig, detectCargoWorkspaces(), detectGoWorkspaces() (+7 more)

### Community 30 - "Package: agent"
Cohesion: 0.08
Nodes (32): Executor Agent, Planner Agent, Reviewer Agent, Security Auditor Agent, Spec Writer Agent, Tester Agent, Autopus-ADK Architecture, 300-Line File Size Limit (+24 more)

### Community 31 - "Package: cmux"
Cohesion: 0.11
Nodes (21): containsArg(), mockExecCommandWithOutput(), newCmuxMockV2(), TestCmuxAdapter_Close_SurfaceRef(), TestCmuxAdapter_Close_WorkspaceName(), TestCmuxAdapter_CreateWorkspace(), TestCmuxAdapter_Notify(), TestCmuxAdapter_SendCommand() (+13 more)

### Community 32 - "Package: backend"
Cohesion: 0.07
Nodes (5): TestNewBackend_CmuxTerminal_ReturnsCmuxBackend(), TestNewBackend_NilTerminal_ReturnsAgentBackend(), TestNewBackend_PlainTerminal_ReturnsAgentBackend(), TestNewBackend_TmuxTerminal_ReturnsAgentBackend(), mockTerminal

### Community 33 - "Package: config"
Cohesion: 0.07
Nodes (27): ArchitectureConf, CommandEntry, ConstraintConf, ContextConf, ExecutorProfileConf, HarnessConfig, HooksConf, IssueReportConf (+19 more)

### Community 34 - "Package: browse"
Cohesion: 0.09
Nodes (6): CmuxBrowserBackend, isCmuxRef(), parseCmuxRef(), parseSurfaceHealth(), validateSignalName(), CmuxAdapter

### Community 35 - "Package: claude"
Cohesion: 0.07
Nodes (2): envContains(), TestClaudeAdapterBuildCommand()

### Community 36 - "Package: cli"
Cohesion: 0.1
Nodes (20): specEntry, rawCredentials, WorkerStatus, checkAuthValidity(), checkDaemonRunning(), CollectStatus(), Error(), Errorf() (+12 more)

### Community 37 - "Package: orchestra"
Cohesion: 0.08
Nodes (5): mockFailBackend, TestIntegration_BackendSelection_Default(), TestIntegration_BackendSelection_Headless(), TestIntegration_BackendSelection_Subprocess(), pipelineMockAdapter

### Community 38 - "Package: cli"
Cohesion: 0.08
Nodes (2): runGit(), TestLoreCommitCmd_AllTrailers()

### Community 39 - "Package: terminal"
Cohesion: 0.07
Nodes (0): 

### Community 40 - "Package: auth"
Cohesion: 0.09
Nodes (6): TestLoadAuthToken_EncryptedFileFallbackAfterPrimaryMiss(), TestSaveCredentials_Permissions(), TestSaveCredentials_ReadOnlyDir(), TestSaveCredentials_WritesFile(), withLegacyCredentialStore(), failingCredentialStore

### Community 41 - "Package: verify"
Cohesion: 0.1
Nodes (8): buildPlaywrightJSON(), TestCollectScreenshots_EmptyPath(), TestCollectScreenshots_EmptySuites(), TestCollectScreenshots_MixedAttachments(), TestCollectScreenshots_MultipleSpecs(), TestCollectScreenshots_NoAttachments(), TestCollectScreenshots_PngSuffixWithoutName(), TestCollectScreenshots_ValidJSON()

### Community 42 - "Package: tui"
Cohesion: 0.08
Nodes (0): 

### Community 43 - "Package: gemini"
Cohesion: 0.08
Nodes (0): 

### Community 44 - "Package: workspace"
Cohesion: 0.08
Nodes (0): 

### Community 45 - "Package: codex"
Cohesion: 0.08
Nodes (0): 

### Community 46 - "Package: cli"
Cohesion: 0.15
Nodes (11): ciRun, Git, extractReportSummary(), fetchRunLogs(), hasGitRemote(), newReactApplyCmd(), newReactCheckCmd(), newReactCmd() (+3 more)

### Community 47 - "Package: gemini"
Cohesion: 0.09
Nodes (0): 

### Community 48 - "Package: control"
Cohesion: 0.18
Nodes (20): applyControlPlaneCapabilities(), canonicalControlPlanePayload(), canonicalSecurityPolicyPayload(), cloneIterationBudget(), hasCapability(), hasControlPlaneMetadata(), hasIterationBudget(), policySignaturePath() (+12 more)

### Community 49 - "Package: cli"
Cohesion: 0.1
Nodes (0): 

### Community 50 - "Package: reviewer"
Cohesion: 0.1
Nodes (0): 

### Community 51 - "Package: hook"
Cohesion: 0.14
Nodes (2): HookResult, HookSession

### Community 52 - "Package: merger"
Cohesion: 0.15
Nodes (13): makeResp(), TestFindDifferences(), TestFindDifferences_CleanOutput_ANSIStripped(), TestFindDifferences_CleanOutput_MCPNoiseExcluded(), TestFindDifferences_SingleResponse(), TestFormatDebate(), TestFormatDebate_CleanOutput_ANSIEscapesRemoved(), TestFormatDebate_CleanOutput_MCPNoiseRemoved() (+5 more)

### Community 53 - "Package: a2a"
Cohesion: 0.15
Nodes (4): Client, ClientConfig, ConnectionState, StateRecoverer

### Community 54 - "Package: progress"
Cohesion: 0.1
Nodes (0): 

### Community 55 - "Package: validate"
Cohesion: 0.1
Nodes (0): 

### Community 56 - "Package: concept"
Cohesion: 0.11
Nodes (20): 5-Phase Multi-Agent Pipeline, AX (Agent Experience) Philosophy, 85% Coverage Gate, Lead-Builder-Guardian Team Roles, Profile Injection into Executor Prompts, Quality Modes (Ultra/Balanced/Adaptive), Test Pyramid Strategy, Autopus-ADK README (Korean) (+12 more)

### Community 57 - "Package: wizard"
Cohesion: 0.11
Nodes (0): 

### Community 58 - "Package: monitor"
Cohesion: 0.14
Nodes (7): currentAddrs(), equal(), ValidateSpecID(), NetMonitor, MonitorSession, MonitorState, PipelineMonitor

### Community 59 - "Package: team"
Cohesion: 0.13
Nodes (6): contains(), containsSubstr(), TestTeamMonitorSession_Close_CleansUp(), TestTeamMonitorSession_Close_TerminalError(), TestTeamMonitorSession_FailedTeammate_Cmux(), TestTeamMonitorSession_Start_SplitPaneFailure()

### Community 60 - "Package: parallel"
Cohesion: 0.15
Nodes (5): WorktreeManager, WorktreeManager, isLockError(), NewWorktreeManager(), sanitizeBranchName()

### Community 61 - "Package: activator"
Cohesion: 0.17
Nodes (12): buildTestRegistry(), TestActivateSkills_AutoActivateFalse(), TestActivateSkills_NoMatch(), TestActivateSkills_ReturnsMatchesAndNotice(), TestMatch_AutoActivateFalse(), TestMatch_CaseInsensitiveKeyword(), TestMatch_KeywordTrigger(), TestMatch_NoMatch() (+4 more)

### Community 62 - "Package: orchestra"
Cohesion: 0.17
Nodes (10): ProgressTracker, providerState, ProviderStatus, ClearProgress(), isTerminal(), LoadProgress(), NewProgressTracker(), progressPath() (+2 more)

### Community 63 - "Package: orchestra"
Cohesion: 0.11
Nodes (0): 

### Community 64 - "Package: integration"
Cohesion: 0.18
Nodes (12): assertDirHasNFiles(), assertDirNotEmpty(), assertFileExists(), runCmd(), TestDoctor_ReportsHealth(), TestE2EInitClaude(), TestE2EInitCodex(), TestE2EInitGemini() (+4 more)

### Community 65 - "Package: dashboard"
Cohesion: 0.11
Nodes (0): 

### Community 66 - "Package: checker"
Cohesion: 0.11
Nodes (0): 

### Community 67 - "Package: interactive"
Cohesion: 0.11
Nodes (0): 

### Community 68 - "Package: manifest"
Cohesion: 0.11
Nodes (0): 

### Community 69 - "Package: codex"
Cohesion: 0.11
Nodes (0): 

### Community 70 - "Package: provider"
Cohesion: 0.11
Nodes (0): 

### Community 71 - "Package: config"
Cohesion: 0.11
Nodes (0): 

### Community 72 - "Package: templates"
Cohesion: 0.11
Nodes (0): 

### Community 73 - "Package: terminal"
Cohesion: 0.15
Nodes (6): setPlainTerminalPath(), TestTerminalNotifyCmd_PlainAdapter(), TestTerminalSendCmd_PlainAdapter(), TestTerminalSplitCmd_PlainAdapter(), TestTerminalWorkspaceCloseCmd_PlainAdapter(), TestTerminalWorkspaceCreateCmd_PlainAdapter()

### Community 74 - "Package: issue"
Cohesion: 0.12
Nodes (0): 

### Community 75 - "Package: framework"
Cohesion: 0.12
Nodes (0): 

### Community 76 - "Package: tmux"
Cohesion: 0.21
Nodes (14): newTmuxErrorMock(), newTmuxMock(), TestTmuxAdapter_Close(), TestTmuxAdapter_Close_Error(), TestTmuxAdapter_CreateWorkspace(), TestTmuxAdapter_CreateWorkspace_Error(), TestTmuxAdapter_CreateWorkspace_NestedSession(), TestTmuxAdapter_Notify() (+6 more)

### Community 77 - "Package: skill"
Cohesion: 0.12
Nodes (0): 

### Community 78 - "Package: coverage"
Cohesion: 0.15
Nodes (6): setupRepo(), TestCheckScope_AllInScope(), TestCheckScope_EmptyAllowedPaths(), TestCheckScope_NoChanges(), TestCheckScope_OutOfScope(), TestSessionFromBranch_NonExperimentBranch()

### Community 79 - "Package: routing"
Cohesion: 0.23
Nodes (11): enabledRoutingConfig(), TestRoutingIntegration_CodexProvider(), TestRoutingIntegration_ComplexPrompt(), TestRoutingIntegration_GeminiProvider(), TestRoutingIntegration_NilRouter(), TestRoutingIntegration_PipelineNilRouter(), TestRoutingIntegration_PipelineSetRouter(), TestRoutingIntegration_TaskConfigModelPropagation() (+3 more)

### Community 80 - "Package: model"
Cohesion: 0.14
Nodes (11): ApprovalRequestMsg, ConnStatus, ConnStatusMsg, CostTracker, CurrentTask, ProviderInfo, TaskCompleteMsg, TaskInfo (+3 more)

### Community 81 - "Package: auth"
Cohesion: 0.12
Nodes (0): 

### Community 82 - "Package: qa"
Cohesion: 0.19
Nodes (8): BuildStage, CleanupStage, ServiceHealthStage, Stage, StageResult, TestStage, runCommand(), validateCommand()

### Community 83 - "Package: doctor"
Cohesion: 0.12
Nodes (0): 

### Community 84 - "Package: permission"
Cohesion: 0.12
Nodes (0): 

### Community 85 - "Package: dashboard"
Cohesion: 0.2
Nodes (14): boxLine(), clampWidth(), FormatElapsed(), renderCurrentTask(), RenderDashboard(), renderHeader(), renderProgressBar(), renderProviders() (+6 more)

### Community 86 - "Package: content"
Cohesion: 0.18
Nodes (10): SkillDefinition, skillFrontmatter, SkillRegistry, convertSkillClaude(), convertSkillCodex(), convertSkillGemini(), ConvertSkillToPlatform(), parseSkillData() (+2 more)

### Community 87 - "Package: profiles"
Cohesion: 0.12
Nodes (0): 

### Community 88 - "Package: orchestra"
Cohesion: 0.21
Nodes (9): emitterSeqMock, emitterSignalMock, newEmitterMock(), TestSignalDetector_WithEmitter_Integration(), TestSignalEmitter_EmitsOnCompletion(), TestSignalEmitter_RoundScopedSignalName(), TestSignalEmitter_SkipsBaseline(), TestSignalEmitter_StopAll() (+1 more)

### Community 89 - "Package: interactive"
Cohesion: 0.22
Nodes (12): CleanScreenForCrossPollination(), cleanScreenOutput(), filterPromptLines(), isPromptLine(), isPromptVisible(), isProviderStillWorking(), isProviderWorking(), isSessionReady() (+4 more)

### Community 90 - "Package: pane"
Cohesion: 0.12
Nodes (0): 

### Community 91 - "Package: docs"
Cohesion: 0.19
Nodes (8): inMemoryCache, stubContext7, stubScraper, newInMemoryCache(), TestFetcher_Context7Primary(), TestFetcher_FallbackToCache(), TestFetcher_FallbackToScraper(), TestFetcher_FallbackToScraper_OnQuotaExceeded()

### Community 92 - "Package: metric"
Cohesion: 0.12
Nodes (0): 

### Community 93 - "Package: loop"
Cohesion: 0.14
Nodes (5): writeResilientAuditEvent(), AuditEvent, auditFailCounter, LogBuffer, slogAuditLogger

### Community 94 - "Package: refresher"
Cohesion: 0.12
Nodes (0): 

### Community 95 - "Package: auth"
Cohesion: 0.17
Nodes (8): captureSrv, slowServerReconnecter, testServerReconnecter, newCredStoreWithCreds(), newRefreshServer(), TestReconnector_DuplicatePrevention(), TestReconnector_SequenceOrder(), TestReconnector_SkipsRefreshIfTokenValid()

### Community 96 - "Package: init"
Cohesion: 0.14
Nodes (2): makeDummyBinary(), TestInitCmd_AutoDetectsSupportedPlatforms()

### Community 97 - "Package: scanner"
Cohesion: 0.3
Nodes (14): detectBuildFiles(), detectEntryPoints(), detectFrameworks(), detectLanguages(), detectTestConfig(), fileExists(), findDirsWithSuffix(), inferDirDescription() (+6 more)

### Community 98 - "Package: profiles"
Cohesion: 0.13
Nodes (0): 

### Community 99 - "Package: orchestra"
Cohesion: 0.26
Nodes (14): paneInfo, buildPaneCommand(), cleanupPanes(), collectPaneResults(), hasSentinel(), mergeByStrategy(), paneArgs(), randomHex() (+6 more)

### Community 100 - "Package: context"
Cohesion: 0.22
Nodes (4): extractFirstParagraph(), extractListItem(), ContextSummarizer, ContextSummarizerConfig

### Community 101 - "Package: opencode"
Cohesion: 0.13
Nodes (0): 

### Community 102 - "Package: issue"
Cohesion: 0.24
Nodes (5): CommandRunner, defaultRunner, ghIssueItem, Submitter, parseIssueNumber()

### Community 103 - "Package: experiment"
Cohesion: 0.18
Nodes (2): Recorder, Recorder

### Community 104 - "Package: auth"
Cohesion: 0.14
Nodes (3): fakeNetError, itoa(), TestBackoff_ExponentialGrowth()

### Community 105 - "Package: model"
Cohesion: 0.13
Nodes (0): 

### Community 106 - "Package: checker"
Cohesion: 0.19
Nodes (9): Check(), checkFile(), filterByCategory(), IsNewerVersion(), matchesExtension(), stripPreRelease(), CheckOptions, Checker (+1 more)

### Community 107 - "Package: query"
Cohesion: 0.31
Nodes (13): checkGitDir(), extractSubject(), hasField(), MatchRelevance(), parseGitLogOutput(), queryByField(), QueryConstraints(), QueryContext() (+5 more)

### Community 108 - "Package: config"
Cohesion: 0.18
Nodes (8): AgentDef, HookDef, PlatformSettings, RuleDef, SkillDef, marshalIndent(), ParseCodexConfig(), parseTOMLLine()

### Community 109 - "Package: conventions"
Cohesion: 0.42
Nodes (13): AnalyzeConventions(), analyzeGoConventions(), analyzeJSConventions(), analyzePythonConventions(), analyzeRustConventions(), analyzeTSConventions(), collectSourceFiles(), detectFileNaming() (+5 more)

### Community 110 - "Package: coverage"
Cohesion: 0.14
Nodes (0): 

### Community 111 - "Package: content"
Cohesion: 0.2
Nodes (12): SessionState, OrchestraSession, SessionProviderConfig, SessionProviderResponse, buildSessionFile(), extractYAMLBlock(), LoadSession(), LoadState() (+4 more)

### Community 112 - "Package: hook"
Cohesion: 0.14
Nodes (0): 

### Community 113 - "Package: orchestra"
Cohesion: 0.14
Nodes (2): fakeCommand, nopWriteCloser

### Community 114 - "Package: strategy"
Cohesion: 0.23
Nodes (9): makeResponse(), TestHandleConsensus_BelowThreshold(), TestHandleConsensus_LowThresholdIncludesMoreLines(), TestHandleConsensus_ThreeResponses(), TestHandleConsensus_UsesConfigThreshold(), TestHandleDebate_NoJudge(), TestHandleDebate_TwoResponses(), TestHandleFastest_SingleResponse() (+1 more)

### Community 115 - "Package: orchestra"
Cohesion: 0.14
Nodes (13): AckOutput, AssumptionOut, ConsensusArea, CrossRisk, DebaterR1Output, DebaterR2Output, Finding, IdeaOutput (+5 more)

### Community 116 - "Package: testutil"
Cohesion: 0.24
Nodes (13): assertFileContains(), assertFileExists(), assertFileNotContains(), assertLineCount(), setupTestDir(), TestAssertFileContains_MultipleSubstrings(), TestAssertFileContains_Pass(), TestAssertFileExists_Pass() (+5 more)

### Community 117 - "Package: docs"
Cohesion: 0.23
Nodes (4): Scraper, ScraperOption, extractGoSection(), stripTags()

### Community 118 - "Package: loop"
Cohesion: 0.14
Nodes (1): successWriter

### Community 119 - "Package: mcp"
Cohesion: 0.14
Nodes (0): 

### Community 120 - "Package: tools"
Cohesion: 0.25
Nodes (11): setupToolTestServer(), TestHandleApproveExecution(), TestHandleExecuteTask(), TestHandleGetExecutionStatus(), TestHandleGetExecutionStatus_MissingID(), TestHandleListAgents(), TestHandleManageWorkspace_Get(), TestHandleManageWorkspace_InvalidParams() (+3 more)

### Community 121 - "Package: adapter"
Cohesion: 0.16
Nodes (4): Registry, Registry, Load(), LoadFromDir()

### Community 122 - "Package: skill"
Cohesion: 0.15
Nodes (0): 

### Community 123 - "Package: cli"
Cohesion: 0.23
Nodes (7): experimentFlags, newExperimentCmd(), newExperimentCommitCmd(), newExperimentInitCmd(), newExperimentMetricCmd(), newExperimentRecordCmd(), newExperimentResetCmd()

### Community 124 - "Package: framework"
Cohesion: 0.15
Nodes (0): 

### Community 125 - "Package: logger"
Cohesion: 0.15
Nodes (0): 

### Community 126 - "Package: schema"
Cohesion: 0.15
Nodes (0): 

### Community 127 - "Package: scanner"
Cohesion: 0.28
Nodes (11): hasDirNamed(), measureDepth(), setupGoProject(), setupJSProject(), TestDetectFrameworks(), TestScan_DirectoryTreeMaxDepth(), TestScan_GoProject(), TestScan_JSProject() (+3 more)

### Community 128 - "Package: prompt"
Cohesion: 0.28
Nodes (12): buildDiscoverInstructions(), BuildReviewPrompt(), buildVerifyInstructions(), CollectContext(), CollectContextForSpec(), collectFilesContext(), extractSourcePaths(), extractSpecContextTargets() (+4 more)

### Community 129 - "Package: skills"
Cohesion: 0.19
Nodes (4): TestSkillRegistry_Get(), TestSkillRegistry_ListByCategory(), TestSkillRegistry_Load(), writeSkillFile()

### Community 130 - "Package: transformer"
Cohesion: 0.15
Nodes (0): 

### Community 131 - "Package: context"
Cohesion: 0.21
Nodes (5): setupTestProject(), TestContextSummarizer_Components(), TestContextSummarizer_PopulatePromptData(), TestContextSummarizer_ScanRelevantPaths(), TestContextSummarizer_Summarize()

### Community 132 - "Package: hook"
Cohesion: 0.15
Nodes (0): 

### Community 133 - "Package: relay"
Cohesion: 0.15
Nodes (0): 

### Community 134 - "Package: round"
Cohesion: 0.15
Nodes (0): 

### Community 135 - "Package: interactive"
Cohesion: 0.15
Nodes (0): 

### Community 136 - "Package: adapter"
Cohesion: 0.18
Nodes (8): Manifest, ManifestFile, UpdateAction, UpdateResult, Checksum(), ManifestFromFiles(), NewManifest(), ResolveAction()

### Community 137 - "Package: context7"
Cohesion: 0.22
Nodes (5): isContext7QuotaError(), wrapContext7APIError(), Context7Client, Context7Client, Context7Option

### Community 138 - "Package: ts"
Cohesion: 0.15
Nodes (0): 

### Community 139 - "Package: extractor"
Cohesion: 0.15
Nodes (0): 

### Community 140 - "Package: analyzer"
Cohesion: 0.33
Nodes (12): Analyze(), analyzeGo(), analyzePython(), analyzeTS(), collectGoPackages(), detectProjectType(), extractGoModule(), fileExists() (+4 more)

### Community 141 - "Package: loop"
Cohesion: 0.22
Nodes (5): TestAuditFailure_DoesNotAffectTaskResult(), TestWriteAuditEvent_Error_LogsWarning(), TestWriteAuditEvent_ThreeConsecutiveFailures_EscalatesToError(), failingAuditWriter, testLogBuffer

### Community 142 - "Package: postconditions"
Cohesion: 0.28
Nodes (12): branchesForVerification(), captureExecutionBaseline(), detectTaskPostconditions(), gitOutput(), gitRun(), mustMarshalPostconditionReport(), sanitizeBranchName(), verifyExecutionPostconditions() (+4 more)

### Community 143 - "Package: auth"
Cohesion: 0.26
Nodes (8): credNotFoundError, fileCredStore, newFileCredStore(), TestLoadCredentials_FileNotFound(), TestLoadSaveCredentials_Roundtrip(), TestRefresh_FiresBeforeExpiry(), TestRefresh_OnReauthNeeded(), TestSaveCredentials_StoreRoundtrip()

### Community 144 - "Package: ws"
Cohesion: 0.22
Nodes (5): TestTransport_ConnectAndSendReceive(), TestTransport_Heartbeat_SendsPing(), TestTransport_Reconnect_Success(), toWSURL(), wsEchoServer()

### Community 145 - "Package: credstore"
Cohesion: 0.28
Nodes (6): decryptGCM(), deriveKey(), encryptGCM(), machinePassphrase(), readMachineID(), encryptedFileStore

### Community 146 - "Package: mcpserver"
Cohesion: 0.21
Nodes (5): cacheEntry, ResourceDescriptor, resourceFetcher, ResourceRegistry, NewResourceRegistry()

### Community 147 - "Package: edge"
Cohesion: 0.15
Nodes (0): 

### Community 148 - "Package: agent"
Cohesion: 0.15
Nodes (13): Preset-Conditional Pipeline Phase Skipping, Agent Presets Skill, ax.go GenerateAXInstruction() Canonical Source, @AX:CYCLE Tracking (TODO Escalation), @AX Annotation Skill, @AX Tag Types (NOTE, WARN, ANCHOR, TODO), Frontend Verify 5-Phase Pipeline, Frontend Verify Skill (+5 more)

### Community 149 - "Package: status"
Cohesion: 0.26
Nodes (7): TestScanSpecs_NonDirectoryEntriesIgnored(), TestStatusCmd_ApprovedStatus(), TestStatusCmd_ImplementedStatusCountsAsDone(), TestStatusCmd_MalformedSpecFile(), TestStatusCmd_MultipleSpecs(), TestStatusCmd_NonSpecDirectoriesIgnored(), writeSpecFile()

### Community 150 - "Package: cache"
Cohesion: 0.24
Nodes (5): sanitizeKey(), Cache, newDocsCacheClearCmd(), newDocsCacheCmd(), newDocsCacheListCmd()

### Community 151 - "Package: learn"
Cohesion: 0.17
Nodes (0): 

### Community 152 - "Package: tui"
Cohesion: 0.27
Nodes (11): InitWizardOpts, InitWizardResult, stepBuilder, buildLangStep(), buildMethodologyStep(), buildQualityStep(), buildReviewGateStep(), buildStepList() (+3 more)

### Community 153 - "Package: hint"
Cohesion: 0.32
Nodes (11): newTestStore(), TestCheckAndShow_EmptyProfileDefaultNone(), TestCheckAndShow_FirstHint(), TestCheckAndShow_FirstHintNotRepeated(), TestCheckAndShow_FullstackProfile(), TestCheckAndShow_HintsDisabled(), TestCheckAndShow_NoHintAfterBoth(), TestCheckAndShow_SecondHintAt3() (+3 more)

### Community 154 - "Package: pipeline"
Cohesion: 0.26
Nodes (1): TeamMonitorSession

### Community 155 - "Package: conventions"
Cohesion: 0.17
Nodes (0): 

### Community 156 - "Package: engine"
Cohesion: 0.17
Nodes (0): 

### Community 157 - "Package: convergence"
Cohesion: 0.17
Nodes (0): 

### Community 158 - "Package: plain"
Cohesion: 0.17
Nodes (1): PlainAdapter

### Community 159 - "Package: agents"
Cohesion: 0.17
Nodes (0): 

### Community 160 - "Package: agent"
Cohesion: 0.21
Nodes (8): buildCodexInstructions(), LoadAgentSources(), LoadAgentSourcesFromFS(), parseAgentSource(), TransformAgentForCodex(), AgentSource, AgentSourceMeta, AgentTransformer

### Community 161 - "Package: skill"
Cohesion: 0.17
Nodes (0): 

### Community 162 - "Package: activator"
Cohesion: 0.17
Nodes (0): 

### Community 163 - "Package: session"
Cohesion: 0.17
Nodes (0): 

### Community 164 - "Package: commands"
Cohesion: 0.17
Nodes (2): Commander, MockClient

### Community 165 - "Package: schema"
Cohesion: 0.18
Nodes (2): TestSchemaBuilder_Generate_DebaterR1Properties(), toStringSlice()

### Community 166 - "Package: warm"
Cohesion: 0.17
Nodes (0): 

### Community 167 - "Package: relay"
Cohesion: 0.17
Nodes (0): 

### Community 168 - "Package: job"
Cohesion: 0.17
Nodes (0): 

### Community 169 - "Package: output"
Cohesion: 0.17
Nodes (0): 

### Community 170 - "Package: opencode"
Cohesion: 0.18
Nodes (1): Adapter

### Community 171 - "Package: extractor"
Cohesion: 0.17
Nodes (0): 

### Community 172 - "Package: policy"
Cohesion: 0.27
Nodes (8): newTestCache(), TestPolicyCacheAtomicWrite(), TestPolicyCacheDelete(), TestPolicyCacheDeleteNonExistent(), TestPolicyCacheFilePermissions(), TestPolicyCacheReadInvalidJSON(), TestPolicyCacheReadNonExistent(), TestPolicyCacheWriteRead()

### Community 173 - "Package: auth"
Cohesion: 0.35
Nodes (8): mockCredentialStore, jsonRefreshResponse(), newMockCredStore(), TestTokenRefresher_BackoffRetry_AllFail_TriggersReauth(), TestTokenRefresher_BackoffRetry_SucceedsOnSecondAttempt(), TestTokenRefresher_CredentialStore_LoadSave(), TestTokenRefresher_ForceRefresh(), TestTokenRefresher_PermanentFailure_401()

### Community 174 - "Package: credstore"
Cohesion: 0.17
Nodes (0): 

### Community 175 - "Package: env"
Cohesion: 0.17
Nodes (0): 

### Community 176 - "Package: install"
Cohesion: 0.42
Nodes (10): Err(), Get-Arch(), Get-GitBashPath(), Get-LatestVersion(), Info(), Main(), Ok(), Show-PathHint() (+2 more)

### Community 177 - "Package: orchestra"
Cohesion: 0.18
Nodes (0): 

### Community 178 - "Package: cli"
Cohesion: 0.18
Nodes (0): 

### Community 179 - "Package: team"
Cohesion: 0.18
Nodes (0): 

### Community 180 - "Package: store"
Cohesion: 0.18
Nodes (0): 

### Community 181 - "Package: migrate"
Cohesion: 0.18
Nodes (0): 

### Community 182 - "Package: agents"
Cohesion: 0.2
Nodes (2): TestLoadAgents(), writeAgentFile()

### Community 183 - "Package: agents"
Cohesion: 0.29
Nodes (10): convertAgentClaude(), convertAgentCodex(), convertAgentGemini(), ConvertAgentToPlatform(), LoadAgents(), LoadAgentsFromFS(), parseAgentData(), parseAgentFile() (+2 more)

### Community 184 - "Package: content"
Cohesion: 0.24
Nodes (9): parsedSkill, SkillMeta, SkillTransformer, TransformedSkill, TransformReport, IsCompatible(), NewSkillTransformer(), NewSkillTransformerFromFS() (+1 more)

### Community 185 - "Package: exclusions"
Cohesion: 0.33
Nodes (9): hasPattern(), TestCommonExclusionsAlwaysPresent(), TestEmptyStackAndFramework(), TestFrameworkPatternsAppended(), TestGoStackExclusions(), TestPythonStackExclusions(), TestRustStackExclusions(), TestTypescriptStackExclusions() (+1 more)

### Community 186 - "Package: content"
Cohesion: 0.25
Nodes (8): ProfileDefinition, profileFrontmatter, LoadProfilesFromDir(), LoadProfilesFromFS(), LoadProfilesFromFSWithWarnings(), parseProfileData(), SelectProfile(), SelectProfileWithConf()

### Community 187 - "Package: agent"
Cohesion: 0.22
Nodes (3): makeExecutorSource(), TestTransformAgentForCodex_RichInstructions(), TestTransformAgentForGemini_Sections()

### Community 188 - "Package: relay"
Cohesion: 0.18
Nodes (0): 

### Community 189 - "Package: prompt"
Cohesion: 0.33
Nodes (9): newTestPromptData(), TestPromptBuilder_BuildDebaterR1(), TestPromptBuilder_BuildDebaterR1_NoSchema(), TestPromptBuilder_BuildDebaterR2(), TestPromptBuilder_BuildJudge(), TestPromptBuilder_BuildReviewer(), TestPromptBuilder_BuildReviewer_NoCodeContext(), TestPromptBuilder_ContextInjected() (+1 more)

### Community 190 - "Package: interactive"
Cohesion: 0.18
Nodes (0): 

### Community 191 - "Package: orchestra"
Cohesion: 0.4
Nodes (4): OutputParser, extractJSON(), stripMarkdownJSON(), tryUnwrapClaudeEnvelope()

### Community 192 - "Package: completion"
Cohesion: 0.18
Nodes (0): 

### Community 193 - "Package: consensus"
Cohesion: 0.18
Nodes (0): 

### Community 194 - "Package: extractor"
Cohesion: 0.49
Nodes (10): makeProject(), TestExtract_ExportedFunc(), TestExtract_GenericFunc(), TestExtract_GenericType(), TestExtract_InterfaceType(), TestExtract_Method(), TestExtract_StructType(), TestExtract_TestFilesSkipped() (+2 more)

### Community 195 - "Package: cli"
Cohesion: 0.33
Nodes (7): docsCacheAdapter, detectLibrariesFromDir(), docsAutoDetect(), docsCacheDir(), docsOutput(), newDocsCmd(), newDocsFetchCmd()

### Community 196 - "Package: config"
Cohesion: 0.51
Nodes (9): chdirTo(), setupConfigDir(), TestConfigGet_HintsPlatform(), TestConfigGet_UsageProfile(), TestConfigSet_HintsPlatform(), TestConfigSet_HintsPlatform_InvalidBool(), TestConfigSet_UnknownKey(), TestConfigSet_UsageProfile() (+1 more)

### Community 197 - "Package: platform"
Cohesion: 0.2
Nodes (0): 

### Community 198 - "Package: update"
Cohesion: 0.2
Nodes (0): 

### Community 199 - "Package: migrate"
Cohesion: 0.2
Nodes (0): 

### Community 200 - "Package: downloader"
Cohesion: 0.27
Nodes (4): buildTarGz(), TestDownloadAndVerify_ChecksumMismatch(), TestDownloadAndVerify_RetrySuccess(), TestDownloadAndVerify_Success()

### Community 201 - "Package: findings"
Cohesion: 0.2
Nodes (0): 

### Community 202 - "Package: content"
Cohesion: 0.33
Nodes (9): GitHookScript, appendUniqueHook(), buildCommitMsgScript(), buildPreCommitScript(), DetectPermissions(), fileExists(), generateCLIHooks(), generateGitHooks() (+1 more)

### Community 203 - "Package: replace"
Cohesion: 0.2
Nodes (0): 

### Community 204 - "Package: activator"
Cohesion: 0.31
Nodes (6): ActivateSkills(), FormatActivationNotice(), isRegexTrigger(), matchSkill(), ActivationResult, SkillActivator

### Community 205 - "Package: intent"
Cohesion: 0.2
Nodes (0): 

### Community 206 - "Package: hooks"
Cohesion: 0.2
Nodes (0): 

### Community 207 - "Package: content"
Cohesion: 0.29
Nodes (7): MethodologyDef, Stage, generateDDDInstruction(), generateDoubleDiamondInstruction(), generateGenericInstruction(), GenerateInstruction(), generateTDDInstruction()

### Community 208 - "Package: activator"
Cohesion: 0.2
Nodes (0): 

### Community 209 - "Package: interactive"
Cohesion: 0.2
Nodes (0): 

### Community 210 - "Package: orchestra"
Cohesion: 0.33
Nodes (6): subprocessBackend, buildSubprocessArgs(), setupStdin(), startWithFileInput(), startWithStdinPipe(), validateJSONOutput()

### Community 211 - "Package: debate"
Cohesion: 0.2
Nodes (0): 

### Community 212 - "Package: orchestra"
Cohesion: 0.24
Nodes (3): mockBackend, defaultOutput(), TestRunSubprocessPipeline_FastMode()

### Community 213 - "Package: extractor"
Cohesion: 0.2
Nodes (0): 

### Community 214 - "Package: cmdvalidate"
Cohesion: 0.2
Nodes (0): 

### Community 215 - "Package: hook"
Cohesion: 0.2
Nodes (0): 

### Community 216 - "Package: agent"
Cohesion: 0.2
Nodes (0): 

### Community 217 - "Package: messages"
Cohesion: 0.2
Nodes (0): 

### Community 218 - "Package: providers"
Cohesion: 0.2
Nodes (0): 

### Community 219 - "Package: status"
Cohesion: 0.31
Nodes (6): TestCheckAuthValidity_APIKey(), TestCheckAuthValidity_ExpiredJWT(), TestCheckAuthValidity_NoExpiryJWT(), TestCheckAuthValidity_UnparseableExpiry(), TestCheckAuthValidity_ValidJWT(), writeCredentials()

### Community 220 - "Package: allocator"
Cohesion: 0.24
Nodes (2): PhaseAllocation, PhaseAllocator

### Community 221 - "Package: scenario"
Cohesion: 0.2
Nodes (0): 

### Community 222 - "Package: checker"
Cohesion: 0.2
Nodes (0): 

### Community 223 - "Package: lsp"
Cohesion: 0.36
Nodes (6): newTestLSPAdapter(), TestLSPClientAdapter_Definition(), TestLSPClientAdapter_Diagnostics(), TestLSPClientAdapter_References(), TestLSPClientAdapter_Rename(), TestLSPClientAdapter_Symbols()

### Community 224 - "Package: pipeline"
Cohesion: 0.25
Nodes (2): makeDummyBinary(), TestResolvePlatform()

### Community 225 - "Package: orchestra"
Cohesion: 0.22
Nodes (0): 

### Community 226 - "Package: detect"
Cohesion: 0.36
Nodes (7): Framework, DetectFramework(), detectFrameworkFromPackageJSON(), detectGoFramework(), detectPythonFramework(), detectRustFramework(), mergeDeps()

### Community 227 - "Package: record"
Cohesion: 0.22
Nodes (0): 

### Community 228 - "Package: platform"
Cohesion: 0.31
Nodes (4): sampleSettings(), TestClaudeJSON_RoundTrip(), TestCodexConfig_RoundTrip(), TestGeminiJSON_RoundTrip()

### Community 229 - "Package: migrate"
Cohesion: 0.39
Nodes (8): containsString(), EnsureOrchestraProvider(), MigrateOpencodeToCodex(), MigrateOrchestraConfig(), MigratePlatformNames(), PlatformToProvider(), ProviderToPlatform(), replaceInSlice()

### Community 230 - "Package: sigmap"
Cohesion: 0.22
Nodes (0): 

### Community 231 - "Package: reviewer"
Cohesion: 0.33
Nodes (6): countActiveFindings(), countEscapeHatch(), parseDiscoverFindings(), ParseVerdict(), parseVerifyFindings(), ShouldTripCircuitBreaker()

### Community 232 - "Package: content"
Cohesion: 0.39
Nodes (8): FileSizeExclusion, commonExclusions(), FileSizeExclusions(), frameworkExclusions(), goExclusions(), pythonExclusions(), rustExclusions(), typescriptExclusions()

### Community 233 - "Package: methodology"
Cohesion: 0.22
Nodes (0): 

### Community 234 - "Package: hook"
Cohesion: 0.22
Nodes (0): 

### Community 235 - "Package: hook"
Cohesion: 0.22
Nodes (0): 

### Community 236 - "Package: interactive"
Cohesion: 0.22
Nodes (0): 

### Community 237 - "Package: iface"
Cohesion: 0.28
Nodes (4): NewExtractorRegistry(), Extractor, ExtractorRegistry, tsExtractorDir

### Community 238 - "Package: loop"
Cohesion: 0.22
Nodes (0): 

### Community 239 - "Package: budget"
Cohesion: 0.22
Nodes (0): 

### Community 240 - "Package: policy"
Cohesion: 0.36
Nodes (2): checkSymlink(), PolicyCache

### Community 241 - "Package: validate"
Cohesion: 0.22
Nodes (0): 

### Community 242 - "Package: backoff"
Cohesion: 0.22
Nodes (0): 

### Community 243 - "Package: approval"
Cohesion: 0.22
Nodes (0): 

### Community 244 - "Package: a2a"
Cohesion: 0.25
Nodes (2): CardBuilder, RegistrationResult

### Community 245 - "Package: credstore"
Cohesion: 0.28
Nodes (6): defaultCredentialDir(), migratePlaintextCredentials(), NewCredentialStore(), CredentialStore, Option, storeOptions

### Community 246 - "Package: apikey"
Cohesion: 0.33
Nodes (5): TestLoadAPIKey_WithAPIKey(), TestLoadAPIKey_WrongAuthType(), TestLoadAuthToken_APIKey(), TestLoadAuthToken_JWT(), writeTestCredentials()

### Community 247 - "Package: audit"
Cohesion: 0.39
Nodes (2): RotatingWriter, NewRotatingWriter()

### Community 248 - "Package: memory"
Cohesion: 0.22
Nodes (0): 

### Community 249 - "Package: handler"
Cohesion: 0.22
Nodes (0): 

### Community 250 - "Package: extract"
Cohesion: 0.5
Nodes (8): findProjectRoot(), makeGoModule(), TestExtractCobra_NestedSubcommands_ExtractsLeafOnly(), TestExtractCobra_NoEntryPoint_ReturnsEmpty(), TestExtractCobra_RealProject_ExtractsKnownCommands(), TestExtractCobra_SimpleCommand_ReturnsScenario(), TestExtractCobra_WithFlags_IncludesFlags(), writeGoFile()

### Community 251 - "Package: runner"
Cohesion: 0.22
Nodes (0): 

### Community 252 - "Package: runner"
Cohesion: 0.22
Nodes (0): 

### Community 253 - "Package: brainstorming"
Cohesion: 0.22
Nodes (9): ICE Scoring, Brainstorming Skill, Discover-Define Phase (Problem Finding), Double Diamond Design Methodology Skill, Idea Skill (Multi-Provider Debate), 2-Round Debate Enforcement, Blind Synthesis Judge (Anti-Bias Subagent), ICE Scoring in Idea Skill (+1 more)

### Community 254 - "Package: docs"
Cohesion: 0.25
Nodes (0): 

### Community 255 - "Package: learn"
Cohesion: 0.54
Nodes (6): chdir(), setupLearnDir(), TestLearnCmd_NoSubcommand_PrintsHelp(), TestLearnQuery_FlagParsing_MultipleFlags(), TestLearnQuery_NoEntries_PrintsNoMatching(), TestLearnQuery_UnknownFlag_ReturnsError()

### Community 256 - "Package: state"
Cohesion: 0.25
Nodes (0): 

### Community 257 - "Package: branchvalidate"
Cohesion: 0.25
Nodes (0): 

### Community 258 - "Package: logger"
Cohesion: 0.32
Nodes (3): formatTextLine(), NewPipelineLogger(), PipelineLogger

### Community 259 - "Package: events"
Cohesion: 0.25
Nodes (5): Event, EventType, Event, InitData, ResultData

### Community 260 - "Package: defaults"
Cohesion: 0.25
Nodes (0): 

### Community 261 - "Package: loader"
Cohesion: 0.25
Nodes (0): 

### Community 262 - "Package: downloader"
Cohesion: 0.39
Nodes (5): extractBinaryTarGz(), extractBinaryZip(), httpGetWithRetry(), ParseChecksums(), Downloader

### Community 263 - "Package: pricing"
Cohesion: 0.25
Nodes (0): 

### Community 264 - "Package: scanner"
Cohesion: 0.25
Nodes (0): 

### Community 265 - "Package: skill"
Cohesion: 0.46
Nodes (7): cleanArg(), replaceAgentCalls(), replaceMCPCalls(), replacePaths(), ReplacePlatformReferences(), replaceTodoWrite(), replaceWorktreeIsolation()

### Community 266 - "Package: agent"
Cohesion: 0.25
Nodes (0): 

### Community 267 - "Package: completion"
Cohesion: 0.43
Nodes (6): newTestHookSession(), TestFileIPCDetector_ContextCancellation(), TestFileIPCDetector_DoneFileExists(), TestFileIPCDetector_RoundDoneFileExists(), TestNewCompletionDetectorWithConfig_FileIPC(), TestNewCompletionDetectorWithConfig_SignalTakesPrecedence()

### Community 268 - "Package: interactive"
Cohesion: 0.29
Nodes (2): consensusReached(), countNonEmpty()

### Community 269 - "Package: merger"
Cohesion: 0.46
Nodes (6): findDifferences(), FormatDebate(), max1(), MergeConsensus(), normalizeLine(), splitLines()

### Community 270 - "Package: hook"
Cohesion: 0.25
Nodes (0): 

### Community 271 - "Package: scraper"
Cohesion: 0.25
Nodes (0): 

### Community 272 - "Package: exa"
Cohesion: 0.29
Nodes (5): NewExaClient(), NewExaClientFromEnv(), ExaClient, ExaOption, SearchResult

### Community 273 - "Package: simplicity"
Cohesion: 0.25
Nodes (0): 

### Community 274 - "Package: circuit"
Cohesion: 0.25
Nodes (0): 

### Community 275 - "Package: pruner"
Cohesion: 0.25
Nodes (0): 

### Community 276 - "Package: autonomous"
Cohesion: 0.25
Nodes (0): 

### Community 277 - "Package: policy"
Cohesion: 0.25
Nodes (0): 

### Community 278 - "Package: control"
Cohesion: 0.25
Nodes (0): 

### Community 279 - "Package: http"
Cohesion: 0.25
Nodes (0): 

### Community 280 - "Package: provider"
Cohesion: 0.5
Nodes (7): checkClaude(), checkCodex(), checkGemini(), checkOpencode(), CheckProviderAuth(), dirExists(), fileExists()

### Community 281 - "Package: mcp"
Cohesion: 0.25
Nodes (3): MCPConfig, MCPConfigOptions, MCPServerConfig

### Community 282 - "Package: cron"
Cohesion: 0.25
Nodes (0): 

### Community 283 - "Package: excluder"
Cohesion: 0.25
Nodes (0): 

### Community 284 - "Package: test"
Cohesion: 0.29
Nodes (0): 

### Community 285 - "Package: gate"
Cohesion: 0.29
Nodes (0): 

### Community 286 - "Package: orchestra"
Cohesion: 0.29
Nodes (0): 

### Community 287 - "Package: cli"
Cohesion: 0.29
Nodes (4): gateChecker, GateConfig, GateMode, GateResult

### Community 288 - "Package: cli"
Cohesion: 0.29
Nodes (6): playwrightAttachment, playwrightResult, playwrightSpec, playwrightSuite, playwrightTest, playwrightTestResult

### Community 289 - "Package: phase"
Cohesion: 0.29
Nodes (4): claudeOutput, codexOutput, geminiOutput, Phase

### Community 290 - "Package: phase"
Cohesion: 0.38
Nodes (2): PhaseContext, PhasePromptBuilder

### Community 291 - "Package: record"
Cohesion: 0.52
Nodes (6): RecordCoverageGap(), recordEntry(), RecordExecutorError(), RecordFixPattern(), RecordGateFail(), RecordReviewIssue()

### Community 292 - "Package: config"
Cohesion: 0.29
Nodes (2): HintsConf, UsageProfile

### Community 293 - "Package: meta"
Cohesion: 0.29
Nodes (0): 

### Community 294 - "Package: findings"
Cohesion: 0.38
Nodes (3): DeduplicateFindings(), MergeSupermajority(), NormalizeScopeRef()

### Community 295 - "Package: generate"
Cohesion: 0.57
Nodes (6): buildSkillTemplate(), generateAgentTemplates(), GenerateAllTemplates(), generateSkillTemplates(), validateName(), writeSkillTemplate()

### Community 296 - "Package: session"
Cohesion: 0.29
Nodes (0): 

### Community 297 - "Package: constraints"
Cohesion: 0.38
Nodes (3): TestGenerateConstraintInstruction_EmptyPatterns(), TestGenerateConstraintInstruction_WithPatterns(), writeConstraintsYAML()

### Community 298 - "Package: activator"
Cohesion: 0.48
Nodes (6): collectSearchDirs(), DetectContext(), detectLanguage(), detectMarkers(), extractExtensions(), ActivationContext

### Community 299 - "Package: router"
Cohesion: 0.38
Nodes (4): GenerateRoutingInstruction(), isKnownCategory(), tierToModel(), Router

### Community 300 - "Package: content"
Cohesion: 0.33
Nodes (5): Phase, Policy, WorkflowDoc, parsePhaseHeader(), ParseWorkflow()

### Community 301 - "Package: screen"
Cohesion: 0.52
Nodes (6): collapseBlankLines(), SanitizeScreenOutput(), stripANSIExtended(), stripCLIBanners(), stripStatusBar(), trimTrailingWhitespace()

### Community 302 - "Package: crosspolinate"
Cohesion: 0.29
Nodes (0): 

### Community 303 - "Package: orchestra"
Cohesion: 0.48
Nodes (3): SchemaBuilder, buildSchema(), fieldSchema()

### Community 304 - "Package: orchestra"
Cohesion: 0.43
Nodes (5): relayStageResult, agenticArgs(), buildRelayPrompt(), cleanupRelayDir(), runRelay()

### Community 305 - "Package: orchestra"
Cohesion: 0.29
Nodes (3): YieldOutput, YieldResponse, YieldRound

### Community 306 - "Package: codex"
Cohesion: 0.52
Nodes (6): codexAgentPipelineSkillBody(), codexAgentTeamsSkillBody(), codexSubagentDevSkillBody(), codexWorktreeIsolationSkillBody(), normalizeCodexExtendedSkill(), rewriteCodexPRDSkillBody()

### Community 307 - "Package: docs"
Cohesion: 0.33
Nodes (2): countingFetcher, TestFetcher_AllSourcesFail()

### Community 308 - "Package: circuit"
Cohesion: 0.29
Nodes (1): CircuitBreaker

### Community 309 - "Package: summarizer"
Cohesion: 0.52
Nodes (6): extractFiles(), extractSections(), Summarize(), truncateToTokens(), writeFileSection(), writeSection()

### Community 310 - "Package: compressor"
Cohesion: 0.29
Nodes (0): 

### Community 311 - "Package: compress"
Cohesion: 0.29
Nodes (3): ContextCompressor, DefaultCompressor, NopCompressor

### Community 312 - "Package: parallel"
Cohesion: 0.29
Nodes (1): TaskSemaphore

### Community 313 - "Package: validate"
Cohesion: 0.29
Nodes (0): 

### Community 314 - "Package: approval"
Cohesion: 0.43
Nodes (6): renderApprovalDialog(), renderApprovalKeys(), renderRiskBadge(), wrapText(), ApprovalRequest, ApprovalResult

### Community 315 - "Package: subagent"
Cohesion: 0.48
Nodes (5): renderChildren(), renderNode(), RenderTree(), statusIcon(), SubagentNode

### Community 316 - "Package: credstore"
Cohesion: 0.29
Nodes (0): 

### Community 317 - "Package: auth"
Cohesion: 0.29
Nodes (0): 

### Community 318 - "Package: cron"
Cohesion: 0.48
Nodes (5): contains(), ParseCron(), parseField(), parsePart(), CronExpr

### Community 319 - "Package: allocator"
Cohesion: 0.29
Nodes (0): 

### Community 320 - "Package: scenario"
Cohesion: 0.29
Nodes (0): 

### Community 321 - "Package: concept"
Cohesion: 0.29
Nodes (7): Lore Commit Format, Autopus Branding Rule, File Size Limit Rule, Language Policy Rule, Lore Commit Rule, Subagent Delegation Rule, Lore Commit Skill

### Community 322 - "Package: config"
Cohesion: 0.6
Nodes (5): applyConfigSet(), getConfigValue(), newConfigCmd(), newConfigGetCmd(), newConfigSetCmd()

### Community 323 - "Package: verify"
Cohesion: 0.33
Nodes (0): 

### Community 324 - "Package: prompts"
Cohesion: 0.6
Nodes (5): newTestCmd(), TestPromptLanguageSettings_AlreadyConfigured(), TestWarnParentRuleConflicts_AutoSetsIsolateRulesWhenPromptSkipped(), TestWarnParentRuleConflicts_IsolateRulesAlreadySet(), TestWarnParentRuleConflicts_NoConflicts()

### Community 325 - "Package: agent"
Cohesion: 0.33
Nodes (0): 

### Community 326 - "Package: agent"
Cohesion: 0.33
Nodes (0): 

### Community 327 - "Package: wizard"
Cohesion: 0.33
Nodes (0): 

### Community 328 - "Package: detect"
Cohesion: 0.53
Nodes (5): packageJSON, detectFromPackageJSON(), DetectTestRunner(), fileExists(), hasPytest()

### Community 329 - "Package: pipeline"
Cohesion: 0.47
Nodes (5): TeamDashboardData, TeammateStatus, NewTeammateStatus(), RenderTeamDashboard(), teammateIcon()

### Community 330 - "Package: events"
Cohesion: 0.33
Nodes (0): 

### Community 331 - "Package: prune"
Cohesion: 0.33
Nodes (0): 

### Community 332 - "Package: summary"
Cohesion: 0.33
Nodes (0): 

### Community 333 - "Package: ensure"
Cohesion: 0.33
Nodes (0): 

### Community 334 - "Package: migrate"
Cohesion: 0.33
Nodes (0): 

### Community 335 - "Package: defaults"
Cohesion: 0.33
Nodes (0): 

### Community 336 - "Package: validator"
Cohesion: 0.47
Nodes (4): isBuildFileName(), Validate(), ValidateCommands(), validateDocFile()

### Community 337 - "Package: sigmap"
Cohesion: 0.33
Nodes (0): 

### Community 338 - "Package: scenarios"
Cohesion: 0.33
Nodes (0): 

### Community 339 - "Package: gherkin"
Cohesion: 0.53
Nodes (4): assignAutoIDs(), normalizeKeyword(), ParseGherkin(), scenarioBuilder

### Community 340 - "Package: content"
Cohesion: 0.4
Nodes (3): IntentRule, GenerateIntentGateInstruction(), sortRulesByPriority()

### Community 341 - "Package: empty"
Cohesion: 0.6
Nodes (5): badArgsProvider(), emptyOutputProvider(), TestRunDebate_JudgeRunsWithPartialResponses(), TestRunParallel_EmptyOutputProviders_AreReportedAsFailed(), TestRunProvider_EmptyOutput_IsAnError()

### Community 342 - "Package: interactive"
Cohesion: 0.33
Nodes (0): 

### Community 343 - "Package: judge"
Cohesion: 0.4
Nodes (3): MergeSubprocessResults(), truncate(), JudgeBuilder

### Community 344 - "Package: interactive"
Cohesion: 0.33
Nodes (0): 

### Community 345 - "Package: codex"
Cohesion: 0.33
Nodes (0): 

### Community 346 - "Package: cache"
Cohesion: 0.33
Nodes (0): 

### Community 347 - "Package: context7"
Cohesion: 0.33
Nodes (0): 

### Community 348 - "Package: docs"
Cohesion: 0.47
Nodes (2): Fetcher, cacheKey()

### Community 349 - "Package: sigmap"
Cohesion: 0.4
Nodes (1): TSExtractor

### Community 350 - "Package: cmdvalidate"
Cohesion: 0.4
Nodes (4): stripSingleQuoted(), ValidateCommand(), validateConfig, ValidateOption

### Community 351 - "Package: reporter"
Cohesion: 0.53
Nodes (4): agentSummary(), FormatComparison(), formatDuration(), FormatSummary()

### Community 352 - "Package: reader"
Cohesion: 0.67
Nodes (5): FilterByType(), LatestPipelineRun(), LoadAllEvents(), LoadEvents(), PipelineRunsBySpecID()

### Community 353 - "Package: pruner"
Cohesion: 0.6
Nodes (5): CountToolBlocks(), PruneAndReport(), pruneBlocks(), PruneSummary(), PruneToolResults()

### Community 354 - "Package: summarizer"
Cohesion: 0.33
Nodes (0): 

### Community 355 - "Package: subagent"
Cohesion: 0.33
Nodes (0): 

### Community 356 - "Package: ensure"
Cohesion: 0.6
Nodes (5): isolatedHome(), TestEnsureWorker_ConfiguredAuthInvalid_RefreshFails(), TestEnsureWorker_ConfiguredAuthValid_DaemonNotRunning(), TestEnsureWorker_NoConfig_DeviceAuthContextCancelled(), TestEnsureWorker_NoConfig_DeviceAuthError()

### Community 357 - "Package: credstore"
Cohesion: 0.33
Nodes (1): keychainStore

### Community 358 - "Package: poll"
Cohesion: 0.47
Nodes (1): TaskPoller

### Community 359 - "Package: warning"
Cohesion: 0.33
Nodes (0): 

### Community 360 - "Package: budget"
Cohesion: 0.47
Nodes (3): WarningInjector, formatDanger(), formatWarning()

### Community 361 - "Package: env"
Cohesion: 0.33
Nodes (0): 

### Community 362 - "Package: e2e"
Cohesion: 0.4
Nodes (4): Scenario, ScenarioSet, renderBuildLine(), RenderScenarios()

### Community 363 - "Package: concept"
Cohesion: 0.33
Nodes (6): EARS Requirements Format, MoSCoW Prioritization, SPEC Document, Document Storage Rule, Planning Skill, PRD Skill

### Community 364 - "Package: subagent"
Cohesion: 0.33
Nodes (6): Agent Definition Format (Claude Code 2.0+), Orchestration Patterns (Fan-Out, Pipeline, Supervisor), Parallel Execution Principle, Subagent Development Skill, File Ownership Conflict Detection, Worktree Isolation Skill

### Community 365 - "Package: skill"
Cohesion: 0.8
Nodes (4): loadSkillRegistry(), newSkillCmd(), runSkillInfo(), runSkillList()

### Community 366 - "Package: docs"
Cohesion: 0.4
Nodes (0): 

### Community 367 - "Package: cli"
Cohesion: 0.6
Nodes (4): scenarioJSONResult, newAutoTestCmd(), newAutoTestRunCmd(), runAutoTest()

### Community 368 - "Package: root"
Cohesion: 0.4
Nodes (0): 

### Community 369 - "Package: test"
Cohesion: 0.6
Nodes (3): TestTestRunCmd_JSONOutput_FormatsCorrectly(), TestTestRunCmd_ValidProject_Succeeds(), writeScenariosFile()

### Community 370 - "Package: skill"
Cohesion: 0.6
Nodes (3): TestSkillInfoCmd(), TestSkillListCmd(), writeTestSkill()

### Community 371 - "Package: box"
Cohesion: 0.4
Nodes (0): 

### Community 372 - "Package: locale"
Cohesion: 0.4
Nodes (0): 

### Community 373 - "Package: cli"
Cohesion: 0.4
Nodes (0): 

### Community 374 - "Package: defaults"
Cohesion: 0.4
Nodes (0): 

### Community 375 - "Package: replacer"
Cohesion: 0.4
Nodes (0): 

### Community 376 - "Package: cost"
Cohesion: 0.5
Nodes (3): ModelPricing, ModelForAgent(), QualityModeToModels()

### Community 377 - "Package: terminal"
Cohesion: 0.4
Nodes (0): 

### Community 378 - "Package: generate"
Cohesion: 0.4
Nodes (0): 

### Community 379 - "Package: hook"
Cohesion: 0.4
Nodes (0): 

### Community 380 - "Package: orchestra"
Cohesion: 0.4
Nodes (4): JudgeResult, PreviousResult, PromptData, RelevantPath

### Community 381 - "Package: graceful"
Cohesion: 0.7
Nodes (4): failProvider(), TestRunOrchestra_GracefulDegradation(), TestRunParallel_AllFail(), TestRunParallel_PartialFailure()

### Community 382 - "Package: yield"
Cohesion: 0.4
Nodes (0): 

### Community 383 - "Package: pane"
Cohesion: 0.5
Nodes (2): shellEscapeArg(), shellEscapeArgs()

### Community 384 - "Package: format"
Cohesion: 0.4
Nodes (0): 

### Community 385 - "Package: sanitizer"
Cohesion: 0.7
Nodes (4): Sanitize(), SanitizeGitURL(), SanitizePath(), SanitizeSecrets()

### Community 386 - "Package: gcm"
Cohesion: 0.4
Nodes (0): 

### Community 387 - "Package: launchd"
Cohesion: 0.4
Nodes (0): 

### Community 388 - "Package: systemd"
Cohesion: 0.4
Nodes (0): 

### Community 389 - "Package: excluder"
Cohesion: 0.4
Nodes (2): Excluder, pattern

### Community 390 - "Package: reaper"
Cohesion: 0.4
Nodes (1): noopDetector

### Community 391 - "Package: reaper"
Cohesion: 0.4
Nodes (1): unixDetector

### Community 392 - "Package: classifier"
Cohesion: 0.4
Nodes (2): ClassificationSignals, MessageComplexityClassifier

### Community 393 - "Package: build"
Cohesion: 0.4
Nodes (1): BuildEntry

### Community 394 - "Package: sync"
Cohesion: 0.4
Nodes (0): 

### Community 395 - "Package: concept"
Cohesion: 0.4
Nodes (5): ANALYZE-PRESERVE-IMPROVE Cycle, @AX:ANCHOR Tag, Branch by Abstraction Pattern, Strangler Fig Pattern, DDD (Disciplined Design Development) Skill

### Community 396 - "Package: orchestra"
Cohesion: 0.83
Nodes (3): buildBrainstormPrompt(), newOrchestraBrainstormCmd(), prependProjectContext()

### Community 397 - "Package: worker"
Cohesion: 0.83
Nodes (3): newWorkerCmd(), newWorkerValidateSubCmd(), runWorkerValidate()

### Community 398 - "Package: worker"
Cohesion: 0.67
Nodes (2): requireNoError(), TestResolveProvider_PrefersAuthenticatedConfiguredProvider()

### Community 399 - "Package: tui"
Cohesion: 0.5
Nodes (1): SummaryRow

### Community 400 - "Package: status"
Cohesion: 0.83
Nodes (3): hasFailedTask(), MapCheckpointToPhases(), resolvePhaseStatus()

### Community 401 - "Package: loader"
Cohesion: 0.67
Nodes (2): expandEnvVars(), Load()

### Community 402 - "Package: migrate"
Cohesion: 0.5
Nodes (0): 

### Community 403 - "Package: protocol"
Cohesion: 0.67
Nodes (2): ParseTrailers(), setField()

### Community 404 - "Package: generate"
Cohesion: 0.5
Nodes (0): 

### Community 405 - "Package: ax"
Cohesion: 0.5
Nodes (0): 

### Community 406 - "Package: agent"
Cohesion: 0.5
Nodes (0): 

### Community 407 - "Package: interactive"
Cohesion: 1.0
Nodes (3): runInteractiveDebate(), runNonInteractiveDebate(), runPaneDebate()

### Community 408 - "Package: interactive"
Cohesion: 0.5
Nodes (0): 

### Community 409 - "Package: consensus"
Cohesion: 0.67
Nodes (2): MergeStructuredConsensus(), parseStructuredResponse()

### Community 410 - "Package: interactive"
Cohesion: 0.5
Nodes (0): 

### Community 411 - "Package: judge"
Cohesion: 0.5
Nodes (0): 

### Community 412 - "Package: writeutil"
Cohesion: 0.5
Nodes (0): 

### Community 413 - "Package: format"
Cohesion: 0.67
Nodes (2): indexOfSubstring(), TestFormat_MultipleLibraries()

### Community 414 - "Package: scraper"
Cohesion: 0.5
Nodes (0): 

### Community 415 - "Package: fanin"
Cohesion: 0.5
Nodes (0): 

### Community 416 - "Package: iface"
Cohesion: 0.5
Nodes (0): 

### Community 417 - "Package: go"
Cohesion: 0.5
Nodes (1): GoExtractor

### Community 418 - "Package: context"
Cohesion: 0.5
Nodes (0): 

### Community 419 - "Package: redos"
Cohesion: 0.5
Nodes (0): 

### Community 420 - "Package: autonomous"
Cohesion: 0.5
Nodes (0): 

### Community 421 - "Package: policy"
Cohesion: 0.67
Nodes (2): cacheSecurityPolicy(), policyDir()

### Community 422 - "Package: parser"
Cohesion: 0.5
Nodes (0): 

### Community 423 - "Package: messages"
Cohesion: 0.67
Nodes (3): HumanError(), HumanErrorf(), errorMapping

### Community 424 - "Package: apikey"
Cohesion: 0.5
Nodes (0): 

### Community 425 - "Package: sse"
Cohesion: 0.5
Nodes (0): 

### Community 426 - "Package: connect"
Cohesion: 0.5
Nodes (1): HeadlessEvent

### Community 427 - "Package: build"
Cohesion: 0.5
Nodes (0): 

### Community 428 - "Package: concept"
Cohesion: 0.67
Nodes (4): Circuit Breaker (XLOOP), Simplicity Gate (XLOOP), XLOOP Experiment Loop, Experiment Loop (XLOOP) Skill

### Community 429 - "Package: ast"
Cohesion: 0.5
Nodes (4): Go AST Tools (gorename, gofmt, gomv), AST Refactoring Skill, Hotspot Analysis (Change Frequency × Complexity), Entropy Scan Skill

### Community 430 - "Package: tdd"
Cohesion: 0.5
Nodes (4): RED-GREEN-REFACTOR Cycle, TDD Skill, Automated Quality Gate, Verification Skill

### Community 431 - "Package: concept"
Cohesion: 0.5
Nodes (3): Bidirectional IPC (SPEC-ORCH-017), Orchestra Engine (Multi-Provider), SPEC Review Gate Skill

### Community 432 - "Package: check"
Cohesion: 1.0
Nodes (2): newCheckCmd(), runChecks()

### Community 433 - "Package: react"
Cohesion: 0.67
Nodes (0): 

### Community 434 - "Package: worker"
Cohesion: 1.0
Nodes (2): a2aSignPolicyForTest(), TestRunWorkerValidate_VerifiesPolicySignature()

### Community 435 - "Package: orchestra"
Cohesion: 0.67
Nodes (0): 

### Community 436 - "Package: orchestra"
Cohesion: 0.67
Nodes (0): 

### Community 437 - "Package: docs"
Cohesion: 0.67
Nodes (0): 

### Community 438 - "Package: update"
Cohesion: 0.67
Nodes (0): 

### Community 439 - "Package: locale"
Cohesion: 1.0
Nodes (2): DetectSystemLang(), matchLang()

### Community 440 - "Package: golden"
Cohesion: 0.67
Nodes (0): 

### Community 441 - "Package: checkpoint"
Cohesion: 1.0
Nodes (2): Load(), LoadWithHash()

### Community 442 - "Package: phase"
Cohesion: 0.67
Nodes (1): GateType

### Community 443 - "Package: review"
Cohesion: 1.0
Nodes (2): formatReviewMd(), PersistReview()

### Community 444 - "Package: validate"
Cohesion: 0.67
Nodes (0): 

### Community 445 - "Package: skill"
Cohesion: 1.0
Nodes (2): containsPlatformRef(), FilterPlatformReferences()

### Community 446 - "Package: hook"
Cohesion: 0.67
Nodes (1): HookInput

### Community 447 - "Package: version"
Cohesion: 0.67
Nodes (0): 

### Community 448 - "Package: linter"
Cohesion: 1.0
Nodes (2): extractLayer(), Lint()

### Community 449 - "Package: policy"
Cohesion: 0.67
Nodes (0): 

### Community 450 - "Package: daemon"
Cohesion: 0.67
Nodes (0): 

### Community 451 - "Package: setup"
Cohesion: 0.67
Nodes (1): workerKeyResponse

### Community 452 - "Package: adapter"
Cohesion: 0.67
Nodes (1): AuditMetadata

### Community 453 - "Package: api"
Cohesion: 0.67
Nodes (3): gRPC Proto Design, RESTful API Design Principles, API Design Skill

### Community 454 - "Package: main"
Cohesion: 1.0
Nodes (0): 

### Community 455 - "Package: init"
Cohesion: 1.0
Nodes (0): 

### Community 456 - "Package: wizard"
Cohesion: 1.0
Nodes (0): 

### Community 457 - "Package: wizard"
Cohesion: 1.0
Nodes (0): 

### Community 458 - "Package: branchvalidate"
Cohesion: 1.0
Nodes (0): 

### Community 459 - "Package: prune"
Cohesion: 1.0
Nodes (0): 

### Community 460 - "Package: summary"
Cohesion: 1.0
Nodes (0): 

### Community 461 - "Package: rewrite"
Cohesion: 1.0
Nodes (0): 

### Community 462 - "Package: defaults"
Cohesion: 1.0
Nodes (0): 

### Community 463 - "Package: writer"
Cohesion: 1.0
Nodes (0): 

### Community 464 - "Package: scenarios"
Cohesion: 1.0
Nodes (0): 

### Community 465 - "Package: ax"
Cohesion: 1.0
Nodes (0): 

### Community 466 - "Package: agent"
Cohesion: 1.0
Nodes (0): 

### Community 467 - "Package: screen"
Cohesion: 1.0
Nodes (0): 

### Community 468 - "Package: writeutil"
Cohesion: 1.0
Nodes (0): 

### Community 469 - "Package: generator"
Cohesion: 1.0
Nodes (0): 

### Community 470 - "Package: simplicity"
Cohesion: 1.0
Nodes (0): 

### Community 471 - "Package: computer"
Cohesion: 1.0
Nodes (0): 

### Community 472 - "Package: validate"
Cohesion: 1.0
Nodes (0): 

### Community 473 - "Package: emergency"
Cohesion: 1.0
Nodes (0): 

### Community 474 - "Package: emergency"
Cohesion: 1.0
Nodes (0): 

### Community 475 - "Package: emergency"
Cohesion: 1.0
Nodes (0): 

### Community 476 - "Package: classifier"
Cohesion: 1.0
Nodes (0): 

### Community 477 - "Package: pidlock"
Cohesion: 1.0
Nodes (0): 

### Community 478 - "Package: flock"
Cohesion: 1.0
Nodes (0): 

### Community 479 - "Package: concept"
Cohesion: 1.0
Nodes (2): Autonomous Experiment Loop, pkg/experiment — Autonomous Experiment Loop

### Community 480 - "Package: concept"
Cohesion: 1.0
Nodes (2): Lore Decision Protocol (9-trailer), pkg/lore — Decision Tracking

### Community 481 - "Package: concept"
Cohesion: 1.0
Nodes (2): E2E Scenario Generation, pkg/e2e — E2E Scenario Engine

### Community 482 - "Package: concept"
Cohesion: 1.0
Nodes (2): Parallel Worktree Execution, Worktree Safety Rule

### Community 483 - "Package: concept"
Cohesion: 1.0
Nodes (2): Context7 MCP Tool, Context7 Documentation Auto-Fetch Rule

### Community 484 - "Package: browser"
Cohesion: 1.0
Nodes (2): Browser Automation Skill, Snapshot-Act-Verify Workflow

### Community 485 - "Package: migration"
Cohesion: 1.0
Nodes (2): Adapter Pattern for Breaking Changes, Migration Skill

### Community 486 - "Package: adaptive"
Cohesion: 1.0
Nodes (2): Complexity-to-Model Mapping Table, Adaptive Quality Skill

### Community 487 - "Package: concept"
Cohesion: 1.0
Nodes (2): SHA256 Hash Anchor File Integrity, Hash-Anchored Edit Skill

### Community 488 - "Package: concept"
Cohesion: 1.0
Nodes (2): Strangler Fig Pattern (Refactoring), Refactoring Skill

### Community 489 - "Package: embed"
Cohesion: 1.0
Nodes (0): 

### Community 490 - "Package: export"
Cohesion: 1.0
Nodes (0): 

### Community 491 - "Package: detect"
Cohesion: 1.0
Nodes (0): 

### Community 492 - "Package: loop"
Cohesion: 1.0
Nodes (0): 

### Community 493 - "Package: server"
Cohesion: 1.0
Nodes (0): 

### Community 494 - "Package: server"
Cohesion: 1.0
Nodes (0): 

### Community 495 - "Package: credstore"
Cohesion: 1.0
Nodes (0): 

### Community 496 - "Package: concept"
Cohesion: 1.0
Nodes (1): Hook-Based Result Collection

### Community 497 - "Package: concept"
Cohesion: 1.0
Nodes (1): Executor Profile System

### Community 498 - "Package: pkg"
Cohesion: 1.0
Nodes (1): pkg/internal/cli — CLI Command Layer

### Community 499 - "Package: pkg"
Cohesion: 1.0
Nodes (1): pkg/adapter — Platform Abstraction (impl)

### Community 500 - "Package: agent"
Cohesion: 1.0
Nodes (1): Validator Agent

### Community 501 - "Package: agent"
Cohesion: 1.0
Nodes (1): Annotator Agent

### Community 502 - "Package: agent"
Cohesion: 1.0
Nodes (1): Architect Agent

### Community 503 - "Package: agent"
Cohesion: 1.0
Nodes (1): Debugger Agent

### Community 504 - "Package: agent"
Cohesion: 1.0
Nodes (1): Explorer Agent

### Community 505 - "Package: agent"
Cohesion: 1.0
Nodes (1): Frontend Specialist Agent

### Community 506 - "Package: agent"
Cohesion: 1.0
Nodes (1): UX Validator Agent

### Community 507 - "Package: agent"
Cohesion: 1.0
Nodes (1): Deep Worker Agent

### Community 508 - "Package: devops"
Cohesion: 1.0
Nodes (1): DevOps Agent

### Community 509 - "Package: perf"
Cohesion: 1.0
Nodes (1): Perf-Engineer Agent

### Community 510 - "Package: rule"
Cohesion: 1.0
Nodes (1): Objective Reasoning Rule

### Community 511 - "Package: rule"
Cohesion: 1.0
Nodes (1): Project Identity Rule

### Community 512 - "Package: skill"
Cohesion: 1.0
Nodes (1): Using Autopus-ADK Skill

### Community 513 - "Package: skill"
Cohesion: 1.0
Nodes (1): Context Search Skill

### Community 514 - "Package: skill"
Cohesion: 1.0
Nodes (1): Playwright CLI Skill

### Community 515 - "Package: concept"
Cohesion: 1.0
Nodes (1): autopus.yaml Configuration

### Community 516 - "Package: concept"
Cohesion: 1.0
Nodes (1): .auto-continue.md Session Continuity File

### Community 517 - "Package: concept"
Cohesion: 1.0
Nodes (1): PRD → Planning → SPEC Pipeline

### Community 518 - "Package: skill"
Cohesion: 1.0
Nodes (1): Debugging Skill

### Community 519 - "Package: skill"
Cohesion: 1.0
Nodes (1): Database Skill

### Community 520 - "Package: concept"
Cohesion: 1.0
Nodes (1): Multi-Stage Docker Build

## Knowledge Gaps
- **548 isolated node(s):** `taskContext`, `taskResult`, `execFunc`, `globalFlags`, `globalFlagsContextKey` (+543 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Package: main`** (2 nodes): `main.go`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: init`** (2 nodes): `init_constraints.go`, `generateDefaultConstraints()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: wizard`** (2 nodes): `wizard_styles.go`, `AutopusTheme()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: wizard`** (2 nodes): `wizard_profile.go`, `buildProfileStep()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: branchvalidate`** (2 nodes): `branchvalidate.go`, `ValidateBranchName()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: prune`** (2 nodes): `prune.go`, `Prune()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: summary`** (2 nodes): `summary.go`, `GenerateSummary()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: rewrite`** (2 nodes): `rewrite.go`, `rewriteStore()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: defaults`** (2 nodes): `defaults.go`, `DefaultFullConfig()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: writer`** (2 nodes): `writer.go`, `BuildCommit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: scenarios`** (2 nodes): `scenarios.go`, `generateScenarios()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: ax`** (2 nodes): `ax.go`, `GenerateAXInstruction()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (2 nodes): `agent_transformer_condense.go`, `condenseBody()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: screen`** (2 nodes): `screen_sanitizer_test.go`, `TestSanitizeScreenOutput()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: writeutil`** (2 nodes): `writeutil.go`, `WriteFileIfChanged()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: generator`** (2 nodes): `generator.go`, `Generate()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: simplicity`** (2 nodes): `simplicity.go`, `CalculateSimplicity()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: computer`** (2 nodes): `computer_use.go`, `ComputerUseSupported()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: validate`** (2 nodes): `validate_normalize.go`, `NormalizeCommand()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: emergency`** (2 nodes): `emergency_unix.go`, `sendSignal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: emergency`** (2 nodes): `emergency_helper_test.go`, `sysProcAttr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: emergency`** (2 nodes): `emergency_windows.go`, `sendSignal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: classifier`** (2 nodes): `classifier_test.go`, `TestClassify()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: pidlock`** (2 nodes): `pidlock_internal_test.go`, `TestAcquire_FlockError()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: flock`** (2 nodes): `flock_unix.go`, `isProcessAlive()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `Autonomous Experiment Loop`, `pkg/experiment — Autonomous Experiment Loop`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `Lore Decision Protocol (9-trailer)`, `pkg/lore — Decision Tracking`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `E2E Scenario Generation`, `pkg/e2e — E2E Scenario Engine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `Parallel Worktree Execution`, `Worktree Safety Rule`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `Context7 MCP Tool`, `Context7 Documentation Auto-Fetch Rule`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: browser`** (2 nodes): `Browser Automation Skill`, `Snapshot-Act-Verify Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: migration`** (2 nodes): `Adapter Pattern for Breaking Changes`, `Migration Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: adaptive`** (2 nodes): `Complexity-to-Model Mapping Table`, `Adaptive Quality Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `SHA256 Hash Anchor File Integrity`, `Hash-Anchored Edit Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (2 nodes): `Strangler Fig Pattern (Refactoring)`, `Refactoring Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: embed`** (1 nodes): `embed.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: export`** (1 nodes): `export_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: detect`** (1 nodes): `detect_stdlib.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: loop`** (1 nodes): `loop_audit_helpers_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: server`** (1 nodes): `server_approval.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: server`** (1 nodes): `server_helpers.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: credstore`** (1 nodes): `credstore_testmain_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `Hook-Based Result Collection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `Executor Profile System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: pkg`** (1 nodes): `pkg/internal/cli — CLI Command Layer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: pkg`** (1 nodes): `pkg/adapter — Platform Abstraction (impl)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Validator Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Annotator Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Architect Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Debugger Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Explorer Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Frontend Specialist Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `UX Validator Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: agent`** (1 nodes): `Deep Worker Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: devops`** (1 nodes): `DevOps Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: perf`** (1 nodes): `Perf-Engineer Agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: rule`** (1 nodes): `Objective Reasoning Rule`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: rule`** (1 nodes): `Project Identity Rule`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: skill`** (1 nodes): `Using Autopus-ADK Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: skill`** (1 nodes): `Context Search Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: skill`** (1 nodes): `Playwright CLI Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `autopus.yaml Configuration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `.auto-continue.md Session Continuity File`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `PRD → Planning → SPEC Pipeline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: skill`** (1 nodes): `Debugging Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: skill`** (1 nodes): `Database Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package: concept`** (1 nodes): `Multi-Stage Docker Build`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Adapter` connect `Codex Adapter` to `Platform Adapter Layer`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **Why does `Adapter` connect `Gemini Adapter` to `Platform Adapter Layer`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `taskContext`, `taskResult`, `execFunc` to the rest of the system?**
  _548 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Platform Adapter Layer` be split into smaller, more focused modules?**
  _Cohesion score 0.0 - nodes in this community are weakly interconnected._
- **Should `A2A Heartbeat & Protocol` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Completion Detection` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Provider Adapter Interfaces` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._