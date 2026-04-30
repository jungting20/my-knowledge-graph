# Graph Report - .  (2026-04-29)

## Corpus Check
- 919 files · ~533,055 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 7590 nodes · 9417 edges · 477 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

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
- `Render()` --calls--> `renderIndex()`  [EXTRACTED]
  raw/autopus-adk/pkg/sigmap/renderer.go → raw/autopus-adk/pkg/setup/renderer.go
- `Render()` --calls--> `renderCommands()`  [EXTRACTED]
  raw/autopus-adk/pkg/sigmap/renderer.go → raw/autopus-adk/pkg/setup/renderer.go
- `Render()` --calls--> `renderStructure()`  [EXTRACTED]
  raw/autopus-adk/pkg/sigmap/renderer.go → raw/autopus-adk/pkg/setup/renderer.go
- `Render()` --calls--> `renderConventions()`  [EXTRACTED]
  raw/autopus-adk/pkg/sigmap/renderer.go → raw/autopus-adk/pkg/setup/renderer.go
- `Render()` --calls--> `renderBoundaries()`  [EXTRACTED]
  raw/autopus-adk/pkg/sigmap/renderer.go → raw/autopus-adk/pkg/setup/renderer.go

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (153): Artifact, ClaudeAdapter, CodexAdapter, codexResultEvent, featureCounts, FileMapping, GeminiAdapter, geminiResultEvent (+145 more)

### Community 1 - "Community 1"
Cohesion: 0.01
Nodes (64): globalFlags, globalFlagsContextKey, applyConfigSet(), getConfigValue(), newConfigCmd(), newConfigGetCmd(), newConfigSetCmd(), chdirTo() (+56 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (66): Heartbeat, LifecycleManager, mockRecoverer, TaskLifecycle, TransitionListener, Transport, TransportConfig, fakeNetError (+58 more)

### Community 3 - "Community 3"
Cohesion: 0.01
Nodes (51): NewPaneBackend(), SelectBackend(), BrowserBackend, SessionID, NewCompletionDetector(), NewCompletionDetectorWithConfig(), signalWaitTimeout(), buildInteractiveLaunchCmd() (+43 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (70): recordParams, Estimator, roundTo6(), TestEstimateCost_BalancedExecutor(), TestEstimateCost_BalancedValidator(), TestEstimateCost_UltraExecutor(), TestEstimatePipelineCost_MultiplePhases(), makePipelineEvent() (+62 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (28): newArchCmd(), newArchEnforceCmd(), newArchGenerateCmd(), checkLore(), checkLoreFromFile(), hasValidLoreType(), isExperimentBranch(), lastCommitMessage() (+20 more)

### Community 6 - "Community 6"
Cohesion: 0.02
Nodes (42): SubprocessPipelineConfig, buildPromptBuilder(), checkpointNotFoundErr(), newPipelineCmd(), newPipelineDashboardCmd(), executeParallel(), FakeBackend, FakeConcurrentBackend (+34 more)

### Community 7 - "Community 7"
Cohesion: 0.02
Nodes (35): deriveChallengeFromVerifier(), extractErrorCode(), PollForToken(), RequestDeviceCode(), tryTokenExchange(), EstimateTokens(), IterationBudget, ShouldCompress() (+27 more)

### Community 8 - "Community 8"
Cohesion: 0.02
Nodes (105): AgentCard, ApprovalRequestParams, ApprovalResponseParams, Artifact, IterationBudget, JSONRPCError, JSONRPCNotification, JSONRPCRequest (+97 more)

### Community 9 - "Community 9"
Cohesion: 0.02
Nodes (54): Credentials, newSuccessDeps(), TestAuthenticateServer_BrowserOpenError(), TestAuthenticateServer_DeviceCodeError(), TestAuthenticateServer_PKCEError(), TestAuthenticateServer_PollTimeout(), TestAuthenticateServer_SaveCredentialsError(), TestAuthenticateServer_Success() (+46 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (67): execFunc, buildJudgmentPrompt(), buildRebuttalPrompt(), findOrBuildJudgeConfig(), runDebate(), runRebuttalRound(), CheckDependencies(), darwinInstallCmd() (+59 more)

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (70): newAgentCmd(), newAgentCreateSubCmd(), parseTools(), runAgentCreate(), validateAgentFrontmatter(), agentFrontmatter, agentTemplateData, skillFrontmatter (+62 more)

### Community 12 - "Community 12"
Cohesion: 0.03
Nodes (27): CollectProviderResult, CollectResult, OrchestraFlags, cleanupJobsInDir(), CleanupStaleJobs(), LoadJob(), newOrchestraCleanupCmd(), runOrchestraCleanup() (+19 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (45): pipelineRunConfig, strategyValue, Runner, RunnerOptions, RunnerResult, learnHookCoverageGap(), learnHookReviewIssue(), mapFindingSeverity() (+37 more)

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (8): lspClientAdapter, createLSPClient(), newLSPCmd(), newLSPDefinitionCmd(), newLSPDiagnosticsCmd(), newLSPRefsCmd(), newLSPRenameCmd(), newLSPSymbolsCmd()

### Community 15 - "Community 15"
Cohesion: 0.04
Nodes (32): Adapter, checksum(), logTransformReport(), fileSizeLimitData, hookEntry, mergeHookCategories(), mergeHooks(), stampAutopusMarker() (+24 more)

### Community 16 - "Community 16"
Cohesion: 0.05
Nodes (21): Server, ServerConfig, TaskHandler, jsonRPCError, jsonRPCRequest, jsonRPCResponse, MCPServer, sseClient (+13 more)

### Community 17 - "Community 17"
Cohesion: 0.04
Nodes (12): newSpecCmd(), newSpecNewCmd(), newSpecValidateCmd(), buildPromptOpts(), buildReviewProviders(), hasActiveFindings(), mergeProviderNames(), newSpecReviewCmd() (+4 more)

### Community 18 - "Community 18"
Cohesion: 0.05
Nodes (15): buildIssueTitle(), confirmIssue(), detectGitRepo(), mockRunner, newIssueCmd(), newIssueListCmd(), newIssueReportCmd(), newIssueSearchCmd() (+7 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (8): TestResolveSingleRun_BySpecID(), TestResolveSingleRun_BySpecID_NotFound(), TestResolveSingleRun_LatestRun(), TestResolveTwoRuns_BySpecID(), TestResolveTwoRuns_BySpecID_NotEnough(), TestResolveTwoRuns_Insufficient(), TestResolveTwoRuns_ReturnsMostRecent(), writeTelemetryEvent()

### Community 20 - "Community 20"
Cohesion: 0.08
Nodes (40): cobraCommand, ExtractCobra(), extractFromFile(), isCobraCommand(), scanCobraCommands(), Extract(), extractFuncSignature(), extractModulePath() (+32 more)

### Community 21 - "Community 21"
Cohesion: 0.05
Nodes (6): TestMonitorSession_Close(), TestMonitorSession_Close_TerminalError(), TestMonitorSession_Close_WithNilTerm(), errorTerminal, failCloseTerminal, mockTerminal

### Community 22 - "Community 22"
Cohesion: 0.07
Nodes (19): Lock, readPIDFromFile(), itoa(), TestAcquire_AlreadyHeld_Error(), addWorkerSubcommands(), installDaemon(), isDaemonInstalled(), newWorkerCostCmd() (+11 more)

### Community 23 - "Community 23"
Cohesion: 0.05
Nodes (7): EntityBrief, GraphContext, KnowledgeSearcher, searchRequest, searchResponse, SearchResult, HashLine

### Community 24 - "Community 24"
Cohesion: 0.07
Nodes (6): Adapter, logTransformReport(), replaceMarkerSection(), mergeSettingsMaps(), mergeUnique(), toStringSlice()

### Community 25 - "Community 25"
Cohesion: 0.06
Nodes (9): mockAdapter, stubAdapter, TestByCategory(), TestGeneratePromptText_Content(), TestLoad_ValidYAML(), TestRegistry_DetectAll(), TestRegistry_RegisterAndGet(), TestRegistryRegisterAndGet() (+1 more)

### Community 26 - "Community 26"
Cohesion: 0.06
Nodes (0): 

### Community 27 - "Community 27"
Cohesion: 0.17
Nodes (28): mockBackend, newMockBackend(), newTestServer(), parseResponse(), TestMCPServer_Initialize(), TestMCPServer_InitializedNotification_IsIgnored(), TestMCPServer_Ping(), TestMCPServer_ResourcesList() (+20 more)

### Community 28 - "Community 28"
Cohesion: 0.08
Nodes (16): CollectContext(), detectPlatform(), lastNLines(), readConfig(), readTelemetry(), hashBytes(), hashProjectStructure(), hashString() (+8 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (15): itoa(), TestCleanupPolicy_FileExists(), Workspace, WorkspaceAgent, nopWriteCloser, WorkspaceConfig, detectCargoWorkspaces(), detectGoWorkspaces() (+7 more)

### Community 30 - "Community 30"
Cohesion: 0.11
Nodes (21): containsArg(), mockExecCommandWithOutput(), newCmuxMockV2(), TestCmuxAdapter_Close_SurfaceRef(), TestCmuxAdapter_Close_WorkspaceName(), TestCmuxAdapter_CreateWorkspace(), TestCmuxAdapter_Notify(), TestCmuxAdapter_SendCommand() (+13 more)

### Community 31 - "Community 31"
Cohesion: 0.07
Nodes (5): TestNewBackend_CmuxTerminal_ReturnsCmuxBackend(), TestNewBackend_NilTerminal_ReturnsAgentBackend(), TestNewBackend_PlainTerminal_ReturnsAgentBackend(), TestNewBackend_TmuxTerminal_ReturnsAgentBackend(), mockTerminal

### Community 32 - "Community 32"
Cohesion: 0.07
Nodes (27): ArchitectureConf, CommandEntry, ConstraintConf, ContextConf, ExecutorProfileConf, HarnessConfig, HooksConf, IssueReportConf (+19 more)

### Community 33 - "Community 33"
Cohesion: 0.09
Nodes (6): CmuxBrowserBackend, isCmuxRef(), parseCmuxRef(), parseSurfaceHealth(), validateSignalName(), CmuxAdapter

### Community 34 - "Community 34"
Cohesion: 0.07
Nodes (2): envContains(), TestClaudeAdapterBuildCommand()

### Community 35 - "Community 35"
Cohesion: 0.1
Nodes (20): specEntry, rawCredentials, WorkerStatus, checkAuthValidity(), checkDaemonRunning(), CollectStatus(), Error(), Errorf() (+12 more)

### Community 36 - "Community 36"
Cohesion: 0.08
Nodes (5): mockFailBackend, TestIntegration_BackendSelection_Default(), TestIntegration_BackendSelection_Headless(), TestIntegration_BackendSelection_Subprocess(), pipelineMockAdapter

### Community 37 - "Community 37"
Cohesion: 0.08
Nodes (2): runGit(), TestLoreCommitCmd_AllTrailers()

### Community 38 - "Community 38"
Cohesion: 0.07
Nodes (0): 

### Community 39 - "Community 39"
Cohesion: 0.09
Nodes (6): TestLoadAuthToken_EncryptedFileFallbackAfterPrimaryMiss(), TestSaveCredentials_Permissions(), TestSaveCredentials_ReadOnlyDir(), TestSaveCredentials_WritesFile(), withLegacyCredentialStore(), failingCredentialStore

### Community 40 - "Community 40"
Cohesion: 0.1
Nodes (8): buildPlaywrightJSON(), TestCollectScreenshots_EmptyPath(), TestCollectScreenshots_EmptySuites(), TestCollectScreenshots_MixedAttachments(), TestCollectScreenshots_MultipleSpecs(), TestCollectScreenshots_NoAttachments(), TestCollectScreenshots_PngSuffixWithoutName(), TestCollectScreenshots_ValidJSON()

### Community 41 - "Community 41"
Cohesion: 0.08
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 0.08
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 0.08
Nodes (0): 

### Community 44 - "Community 44"
Cohesion: 0.08
Nodes (0): 

### Community 45 - "Community 45"
Cohesion: 0.09
Nodes (0): 

### Community 46 - "Community 46"
Cohesion: 0.09
Nodes (0): 

### Community 47 - "Community 47"
Cohesion: 0.18
Nodes (20): applyControlPlaneCapabilities(), canonicalControlPlanePayload(), canonicalSecurityPolicyPayload(), cloneIterationBudget(), hasCapability(), hasControlPlaneMetadata(), hasIterationBudget(), policySignaturePath() (+12 more)

### Community 48 - "Community 48"
Cohesion: 0.1
Nodes (0): 

### Community 49 - "Community 49"
Cohesion: 0.1
Nodes (0): 

### Community 50 - "Community 50"
Cohesion: 0.14
Nodes (2): HookResult, HookSession

### Community 51 - "Community 51"
Cohesion: 0.15
Nodes (13): makeResp(), TestFindDifferences(), TestFindDifferences_CleanOutput_ANSIStripped(), TestFindDifferences_CleanOutput_MCPNoiseExcluded(), TestFindDifferences_SingleResponse(), TestFormatDebate(), TestFormatDebate_CleanOutput_ANSIEscapesRemoved(), TestFormatDebate_CleanOutput_MCPNoiseRemoved() (+5 more)

### Community 52 - "Community 52"
Cohesion: 0.15
Nodes (4): Client, ClientConfig, ConnectionState, StateRecoverer

### Community 53 - "Community 53"
Cohesion: 0.1
Nodes (0): 

### Community 54 - "Community 54"
Cohesion: 0.1
Nodes (4): countingScreenMock, mockTerminal, pipePaneErrorMock, sendLongTextErrorMock

### Community 55 - "Community 55"
Cohesion: 0.1
Nodes (0): 

### Community 56 - "Community 56"
Cohesion: 0.11
Nodes (0): 

### Community 57 - "Community 57"
Cohesion: 0.14
Nodes (7): currentAddrs(), equal(), ValidateSpecID(), NetMonitor, MonitorSession, MonitorState, PipelineMonitor

### Community 58 - "Community 58"
Cohesion: 0.13
Nodes (6): contains(), containsSubstr(), TestTeamMonitorSession_Close_CleansUp(), TestTeamMonitorSession_Close_TerminalError(), TestTeamMonitorSession_FailedTeammate_Cmux(), TestTeamMonitorSession_Start_SplitPaneFailure()

### Community 59 - "Community 59"
Cohesion: 0.17
Nodes (12): buildTestRegistry(), TestActivateSkills_AutoActivateFalse(), TestActivateSkills_NoMatch(), TestActivateSkills_ReturnsMatchesAndNotice(), TestMatch_AutoActivateFalse(), TestMatch_CaseInsensitiveKeyword(), TestMatch_KeywordTrigger(), TestMatch_NoMatch() (+4 more)

### Community 60 - "Community 60"
Cohesion: 0.17
Nodes (10): ProgressTracker, providerState, ProviderStatus, ClearProgress(), isTerminal(), LoadProgress(), NewProgressTracker(), progressPath() (+2 more)

### Community 61 - "Community 61"
Cohesion: 0.18
Nodes (12): assertDirHasNFiles(), assertDirNotEmpty(), assertFileExists(), runCmd(), TestDoctor_ReportsHealth(), TestE2EInitClaude(), TestE2EInitCodex(), TestE2EInitGemini() (+4 more)

### Community 62 - "Community 62"
Cohesion: 0.11
Nodes (0): 

### Community 63 - "Community 63"
Cohesion: 0.11
Nodes (0): 

### Community 64 - "Community 64"
Cohesion: 0.11
Nodes (0): 

### Community 65 - "Community 65"
Cohesion: 0.11
Nodes (0): 

### Community 66 - "Community 66"
Cohesion: 0.11
Nodes (0): 

### Community 67 - "Community 67"
Cohesion: 0.11
Nodes (0): 

### Community 68 - "Community 68"
Cohesion: 0.11
Nodes (0): 

### Community 69 - "Community 69"
Cohesion: 0.15
Nodes (6): setPlainTerminalPath(), TestTerminalNotifyCmd_PlainAdapter(), TestTerminalSendCmd_PlainAdapter(), TestTerminalSplitCmd_PlainAdapter(), TestTerminalWorkspaceCloseCmd_PlainAdapter(), TestTerminalWorkspaceCreateCmd_PlainAdapter()

### Community 70 - "Community 70"
Cohesion: 0.12
Nodes (0): 

### Community 71 - "Community 71"
Cohesion: 0.12
Nodes (0): 

### Community 72 - "Community 72"
Cohesion: 0.12
Nodes (0): 

### Community 73 - "Community 73"
Cohesion: 0.21
Nodes (14): newTmuxErrorMock(), newTmuxMock(), TestTmuxAdapter_Close(), TestTmuxAdapter_Close_Error(), TestTmuxAdapter_CreateWorkspace(), TestTmuxAdapter_CreateWorkspace_Error(), TestTmuxAdapter_CreateWorkspace_NestedSession(), TestTmuxAdapter_Notify() (+6 more)

### Community 74 - "Community 74"
Cohesion: 0.12
Nodes (0): 

### Community 75 - "Community 75"
Cohesion: 0.12
Nodes (1): failNSendLongTextMock

### Community 76 - "Community 76"
Cohesion: 0.15
Nodes (6): setupRepo(), TestCheckScope_AllInScope(), TestCheckScope_EmptyAllowedPaths(), TestCheckScope_NoChanges(), TestCheckScope_OutOfScope(), TestSessionFromBranch_NonExperimentBranch()

### Community 77 - "Community 77"
Cohesion: 0.23
Nodes (11): enabledRoutingConfig(), TestRoutingIntegration_CodexProvider(), TestRoutingIntegration_ComplexPrompt(), TestRoutingIntegration_GeminiProvider(), TestRoutingIntegration_NilRouter(), TestRoutingIntegration_PipelineNilRouter(), TestRoutingIntegration_PipelineSetRouter(), TestRoutingIntegration_TaskConfigModelPropagation() (+3 more)

### Community 78 - "Community 78"
Cohesion: 0.14
Nodes (11): ApprovalRequestMsg, ConnStatus, ConnStatusMsg, CostTracker, CurrentTask, ProviderInfo, TaskCompleteMsg, TaskInfo (+3 more)

### Community 79 - "Community 79"
Cohesion: 0.12
Nodes (0): 

### Community 80 - "Community 80"
Cohesion: 0.19
Nodes (8): BuildStage, CleanupStage, ServiceHealthStage, Stage, StageResult, TestStage, runCommand(), validateCommand()

### Community 81 - "Community 81"
Cohesion: 0.12
Nodes (0): 

### Community 82 - "Community 82"
Cohesion: 0.2
Nodes (14): boxLine(), clampWidth(), FormatElapsed(), renderCurrentTask(), RenderDashboard(), renderHeader(), renderProgressBar(), renderProviders() (+6 more)

### Community 83 - "Community 83"
Cohesion: 0.18
Nodes (10): SkillDefinition, skillFrontmatter, SkillRegistry, convertSkillClaude(), convertSkillCodex(), convertSkillGemini(), ConvertSkillToPlatform(), parseSkillData() (+2 more)

### Community 84 - "Community 84"
Cohesion: 0.12
Nodes (0): 

### Community 85 - "Community 85"
Cohesion: 0.21
Nodes (9): emitterSeqMock, emitterSignalMock, newEmitterMock(), TestSignalDetector_WithEmitter_Integration(), TestSignalEmitter_EmitsOnCompletion(), TestSignalEmitter_RoundScopedSignalName(), TestSignalEmitter_SkipsBaseline(), TestSignalEmitter_StopAll() (+1 more)

### Community 86 - "Community 86"
Cohesion: 0.22
Nodes (12): CleanScreenForCrossPollination(), cleanScreenOutput(), filterPromptLines(), isPromptLine(), isPromptVisible(), isProviderStillWorking(), isProviderWorking(), isSessionReady() (+4 more)

### Community 87 - "Community 87"
Cohesion: 0.12
Nodes (0): 

### Community 88 - "Community 88"
Cohesion: 0.19
Nodes (8): inMemoryCache, stubContext7, stubScraper, newInMemoryCache(), TestFetcher_Context7Primary(), TestFetcher_FallbackToCache(), TestFetcher_FallbackToScraper(), TestFetcher_FallbackToScraper_OnQuotaExceeded()

### Community 89 - "Community 89"
Cohesion: 0.12
Nodes (0): 

### Community 90 - "Community 90"
Cohesion: 0.14
Nodes (5): writeResilientAuditEvent(), AuditEvent, auditFailCounter, LogBuffer, slogAuditLogger

### Community 91 - "Community 91"
Cohesion: 0.12
Nodes (0): 

### Community 92 - "Community 92"
Cohesion: 0.17
Nodes (8): captureSrv, slowServerReconnecter, testServerReconnecter, newCredStoreWithCreds(), newRefreshServer(), TestReconnector_DuplicatePrevention(), TestReconnector_SequenceOrder(), TestReconnector_SkipsRefreshIfTokenValid()

### Community 93 - "Community 93"
Cohesion: 0.21
Nodes (9): CallbackRequest, OAuthConfig, OAuthFlowResult, OAuthResult, buildAuthorizeURL(), callbackHandler(), ExchangeAuthCode(), StartOAuthFlow() (+1 more)

### Community 94 - "Community 94"
Cohesion: 0.14
Nodes (2): makeDummyBinary(), TestInitCmd_AutoDetectsSupportedPlatforms()

### Community 95 - "Community 95"
Cohesion: 0.19
Nodes (9): Check(), checkFile(), filterByCategory(), IsNewerVersion(), matchesExtension(), stripPreRelease(), CheckOptions, Checker (+1 more)

### Community 96 - "Community 96"
Cohesion: 0.3
Nodes (14): detectBuildFiles(), detectEntryPoints(), detectFrameworks(), detectLanguages(), detectTestConfig(), fileExists(), findDirsWithSuffix(), inferDirDescription() (+6 more)

### Community 97 - "Community 97"
Cohesion: 0.13
Nodes (0): 

### Community 98 - "Community 98"
Cohesion: 0.22
Nodes (4): extractFirstParagraph(), extractListItem(), ContextSummarizer, ContextSummarizerConfig

### Community 99 - "Community 99"
Cohesion: 0.13
Nodes (0): 

### Community 100 - "Community 100"
Cohesion: 0.24
Nodes (5): CommandRunner, defaultRunner, ghIssueItem, Submitter, parseIssueNumber()

### Community 101 - "Community 101"
Cohesion: 0.18
Nodes (2): Recorder, Recorder

### Community 102 - "Community 102"
Cohesion: 0.13
Nodes (0): 

### Community 103 - "Community 103"
Cohesion: 0.31
Nodes (13): checkGitDir(), extractSubject(), hasField(), MatchRelevance(), parseGitLogOutput(), queryByField(), QueryConstraints(), QueryContext() (+5 more)

### Community 104 - "Community 104"
Cohesion: 0.18
Nodes (8): AgentDef, HookDef, PlatformSettings, RuleDef, SkillDef, marshalIndent(), ParseCodexConfig(), parseTOMLLine()

### Community 105 - "Community 105"
Cohesion: 0.42
Nodes (13): AnalyzeConventions(), analyzeGoConventions(), analyzeJSConventions(), analyzePythonConventions(), analyzeRustConventions(), analyzeTSConventions(), collectSourceFiles(), detectFileNaming() (+5 more)

### Community 106 - "Community 106"
Cohesion: 0.14
Nodes (0): 

### Community 107 - "Community 107"
Cohesion: 0.2
Nodes (12): SessionState, OrchestraSession, SessionProviderConfig, SessionProviderResponse, buildSessionFile(), extractYAMLBlock(), LoadSession(), LoadState() (+4 more)

### Community 108 - "Community 108"
Cohesion: 0.14
Nodes (0): 

### Community 109 - "Community 109"
Cohesion: 0.14
Nodes (2): fakeCommand, nopWriteCloser

### Community 110 - "Community 110"
Cohesion: 0.23
Nodes (9): makeResponse(), TestHandleConsensus_BelowThreshold(), TestHandleConsensus_LowThresholdIncludesMoreLines(), TestHandleConsensus_ThreeResponses(), TestHandleConsensus_UsesConfigThreshold(), TestHandleDebate_NoJudge(), TestHandleDebate_TwoResponses(), TestHandleFastest_SingleResponse() (+1 more)

### Community 111 - "Community 111"
Cohesion: 0.14
Nodes (13): AckOutput, AssumptionOut, ConsensusArea, CrossRisk, DebaterR1Output, DebaterR2Output, Finding, IdeaOutput (+5 more)

### Community 112 - "Community 112"
Cohesion: 0.24
Nodes (13): assertFileContains(), assertFileExists(), assertFileNotContains(), assertLineCount(), setupTestDir(), TestAssertFileContains_MultipleSubstrings(), TestAssertFileContains_Pass(), TestAssertFileExists_Pass() (+5 more)

### Community 113 - "Community 113"
Cohesion: 0.23
Nodes (4): Scraper, ScraperOption, extractGoSection(), stripTags()

### Community 114 - "Community 114"
Cohesion: 0.14
Nodes (1): successWriter

### Community 115 - "Community 115"
Cohesion: 0.14
Nodes (0): 

### Community 116 - "Community 116"
Cohesion: 0.25
Nodes (11): setupToolTestServer(), TestHandleApproveExecution(), TestHandleExecuteTask(), TestHandleGetExecutionStatus(), TestHandleGetExecutionStatus_MissingID(), TestHandleListAgents(), TestHandleManageWorkspace_Get(), TestHandleManageWorkspace_InvalidParams() (+3 more)

### Community 117 - "Community 117"
Cohesion: 0.16
Nodes (4): Registry, Registry, Load(), LoadFromDir()

### Community 118 - "Community 118"
Cohesion: 0.15
Nodes (0): 

### Community 119 - "Community 119"
Cohesion: 0.23
Nodes (7): experimentFlags, newExperimentCmd(), newExperimentCommitCmd(), newExperimentInitCmd(), newExperimentMetricCmd(), newExperimentRecordCmd(), newExperimentResetCmd()

### Community 120 - "Community 120"
Cohesion: 0.15
Nodes (0): 

### Community 121 - "Community 121"
Cohesion: 0.15
Nodes (0): 

### Community 122 - "Community 122"
Cohesion: 0.15
Nodes (0): 

### Community 123 - "Community 123"
Cohesion: 0.28
Nodes (11): hasDirNamed(), measureDepth(), setupGoProject(), setupJSProject(), TestDetectFrameworks(), TestScan_DirectoryTreeMaxDepth(), TestScan_GoProject(), TestScan_JSProject() (+3 more)

### Community 124 - "Community 124"
Cohesion: 0.28
Nodes (12): buildDiscoverInstructions(), BuildReviewPrompt(), buildVerifyInstructions(), CollectContext(), CollectContextForSpec(), collectFilesContext(), extractSourcePaths(), extractSpecContextTargets() (+4 more)

### Community 125 - "Community 125"
Cohesion: 0.19
Nodes (4): TestSkillRegistry_Get(), TestSkillRegistry_ListByCategory(), TestSkillRegistry_Load(), writeSkillFile()

### Community 126 - "Community 126"
Cohesion: 0.15
Nodes (0): 

### Community 127 - "Community 127"
Cohesion: 0.21
Nodes (5): setupTestProject(), TestContextSummarizer_Components(), TestContextSummarizer_PopulatePromptData(), TestContextSummarizer_ScanRelevantPaths(), TestContextSummarizer_Summarize()

### Community 128 - "Community 128"
Cohesion: 0.15
Nodes (0): 

### Community 129 - "Community 129"
Cohesion: 0.15
Nodes (0): 

### Community 130 - "Community 130"
Cohesion: 0.15
Nodes (0): 

### Community 131 - "Community 131"
Cohesion: 0.23
Nodes (1): SurfaceManager

### Community 132 - "Community 132"
Cohesion: 0.15
Nodes (0): 

### Community 133 - "Community 133"
Cohesion: 0.18
Nodes (8): Manifest, ManifestFile, UpdateAction, UpdateResult, Checksum(), ManifestFromFiles(), NewManifest(), ResolveAction()

### Community 134 - "Community 134"
Cohesion: 0.22
Nodes (5): isContext7QuotaError(), wrapContext7APIError(), Context7Client, Context7Client, Context7Option

### Community 135 - "Community 135"
Cohesion: 0.15
Nodes (0): 

### Community 136 - "Community 136"
Cohesion: 0.15
Nodes (0): 

### Community 137 - "Community 137"
Cohesion: 0.33
Nodes (12): Analyze(), analyzeGo(), analyzePython(), analyzeTS(), collectGoPackages(), detectProjectType(), extractGoModule(), fileExists() (+4 more)

### Community 138 - "Community 138"
Cohesion: 0.22
Nodes (5): TestAuditFailure_DoesNotAffectTaskResult(), TestWriteAuditEvent_Error_LogsWarning(), TestWriteAuditEvent_ThreeConsecutiveFailures_EscalatesToError(), failingAuditWriter, testLogBuffer

### Community 139 - "Community 139"
Cohesion: 0.26
Nodes (8): credNotFoundError, fileCredStore, newFileCredStore(), TestLoadCredentials_FileNotFound(), TestLoadSaveCredentials_Roundtrip(), TestRefresh_FiresBeforeExpiry(), TestRefresh_OnReauthNeeded(), TestSaveCredentials_StoreRoundtrip()

### Community 140 - "Community 140"
Cohesion: 0.22
Nodes (5): TestTransport_ConnectAndSendReceive(), TestTransport_Heartbeat_SendsPing(), TestTransport_Reconnect_Success(), toWSURL(), wsEchoServer()

### Community 141 - "Community 141"
Cohesion: 0.28
Nodes (6): decryptGCM(), deriveKey(), encryptGCM(), machinePassphrase(), readMachineID(), encryptedFileStore

### Community 142 - "Community 142"
Cohesion: 0.15
Nodes (0): 

### Community 143 - "Community 143"
Cohesion: 0.26
Nodes (7): TestScanSpecs_NonDirectoryEntriesIgnored(), TestStatusCmd_ApprovedStatus(), TestStatusCmd_ImplementedStatusCountsAsDone(), TestStatusCmd_MalformedSpecFile(), TestStatusCmd_MultipleSpecs(), TestStatusCmd_NonSpecDirectoriesIgnored(), writeSpecFile()

### Community 144 - "Community 144"
Cohesion: 0.24
Nodes (5): sanitizeKey(), Cache, newDocsCacheClearCmd(), newDocsCacheCmd(), newDocsCacheListCmd()

### Community 145 - "Community 145"
Cohesion: 0.17
Nodes (0): 

### Community 146 - "Community 146"
Cohesion: 0.27
Nodes (11): InitWizardOpts, InitWizardResult, stepBuilder, buildLangStep(), buildMethodologyStep(), buildQualityStep(), buildReviewGateStep(), buildStepList() (+3 more)

### Community 147 - "Community 147"
Cohesion: 0.17
Nodes (0): 

### Community 148 - "Community 148"
Cohesion: 0.17
Nodes (0): 

### Community 149 - "Community 149"
Cohesion: 0.17
Nodes (0): 

### Community 150 - "Community 150"
Cohesion: 0.17
Nodes (0): 

### Community 151 - "Community 151"
Cohesion: 0.2
Nodes (2): TmuxAdapter, buildTmuxCreateCmd()

### Community 152 - "Community 152"
Cohesion: 0.17
Nodes (1): PlainAdapter

### Community 153 - "Community 153"
Cohesion: 0.17
Nodes (0): 

### Community 154 - "Community 154"
Cohesion: 0.21
Nodes (8): buildCodexInstructions(), LoadAgentSources(), LoadAgentSourcesFromFS(), parseAgentSource(), TransformAgentForCodex(), AgentSource, AgentSourceMeta, AgentTransformer

### Community 155 - "Community 155"
Cohesion: 0.17
Nodes (0): 

### Community 156 - "Community 156"
Cohesion: 0.17
Nodes (0): 

### Community 157 - "Community 157"
Cohesion: 0.17
Nodes (0): 

### Community 158 - "Community 158"
Cohesion: 0.17
Nodes (2): Commander, MockClient

### Community 159 - "Community 159"
Cohesion: 0.18
Nodes (2): TestSchemaBuilder_Generate_DebaterR1Properties(), toStringSlice()

### Community 160 - "Community 160"
Cohesion: 0.17
Nodes (0): 

### Community 161 - "Community 161"
Cohesion: 0.17
Nodes (0): 

### Community 162 - "Community 162"
Cohesion: 0.17
Nodes (0): 

### Community 163 - "Community 163"
Cohesion: 0.17
Nodes (0): 

### Community 164 - "Community 164"
Cohesion: 0.18
Nodes (1): Adapter

### Community 165 - "Community 165"
Cohesion: 0.17
Nodes (0): 

### Community 166 - "Community 166"
Cohesion: 0.3
Nodes (1): Git

### Community 167 - "Community 167"
Cohesion: 0.27
Nodes (8): newTestCache(), TestPolicyCacheAtomicWrite(), TestPolicyCacheDelete(), TestPolicyCacheDeleteNonExistent(), TestPolicyCacheFilePermissions(), TestPolicyCacheReadInvalidJSON(), TestPolicyCacheReadNonExistent(), TestPolicyCacheWriteRead()

### Community 168 - "Community 168"
Cohesion: 0.35
Nodes (8): mockCredentialStore, jsonRefreshResponse(), newMockCredStore(), TestTokenRefresher_BackoffRetry_AllFail_TriggersReauth(), TestTokenRefresher_BackoffRetry_SucceedsOnSecondAttempt(), TestTokenRefresher_CredentialStore_LoadSave(), TestTokenRefresher_ForceRefresh(), TestTokenRefresher_PermanentFailure_401()

### Community 169 - "Community 169"
Cohesion: 0.23
Nodes (5): pollResponse, PollResult, RESTPoller, RESTPollerConfig, decodePollTasks()

### Community 170 - "Community 170"
Cohesion: 0.17
Nodes (0): 

### Community 171 - "Community 171"
Cohesion: 0.17
Nodes (0): 

### Community 172 - "Community 172"
Cohesion: 0.42
Nodes (10): Err(), Get-Arch(), Get-GitBashPath(), Get-LatestVersion(), Info(), Main(), Ok(), Show-PathHint() (+2 more)

### Community 173 - "Community 173"
Cohesion: 0.18
Nodes (0): 

### Community 174 - "Community 174"
Cohesion: 0.33
Nodes (10): ciRun, extractReportSummary(), fetchRunLogs(), hasGitRemote(), newReactApplyCmd(), newReactCheckCmd(), newReactCmd(), runReactApply() (+2 more)

### Community 175 - "Community 175"
Cohesion: 0.18
Nodes (0): 

### Community 176 - "Community 176"
Cohesion: 0.18
Nodes (0): 

### Community 177 - "Community 177"
Cohesion: 0.18
Nodes (0): 

### Community 178 - "Community 178"
Cohesion: 0.18
Nodes (0): 

### Community 179 - "Community 179"
Cohesion: 0.2
Nodes (2): TestLoadAgents(), writeAgentFile()

### Community 180 - "Community 180"
Cohesion: 0.29
Nodes (10): convertAgentClaude(), convertAgentCodex(), convertAgentGemini(), ConvertAgentToPlatform(), LoadAgents(), LoadAgentsFromFS(), parseAgentData(), parseAgentFile() (+2 more)

### Community 181 - "Community 181"
Cohesion: 0.24
Nodes (9): parsedSkill, SkillMeta, SkillTransformer, TransformedSkill, TransformReport, IsCompatible(), NewSkillTransformer(), NewSkillTransformerFromFS() (+1 more)

### Community 182 - "Community 182"
Cohesion: 0.33
Nodes (9): hasPattern(), TestCommonExclusionsAlwaysPresent(), TestEmptyStackAndFramework(), TestFrameworkPatternsAppended(), TestGoStackExclusions(), TestPythonStackExclusions(), TestRustStackExclusions(), TestTypescriptStackExclusions() (+1 more)

### Community 183 - "Community 183"
Cohesion: 0.25
Nodes (8): ProfileDefinition, profileFrontmatter, LoadProfilesFromDir(), LoadProfilesFromFS(), LoadProfilesFromFSWithWarnings(), parseProfileData(), SelectProfile(), SelectProfileWithConf()

### Community 184 - "Community 184"
Cohesion: 0.22
Nodes (3): makeExecutorSource(), TestTransformAgentForCodex_RichInstructions(), TestTransformAgentForGemini_Sections()

### Community 185 - "Community 185"
Cohesion: 0.18
Nodes (0): 

### Community 186 - "Community 186"
Cohesion: 0.33
Nodes (9): newTestPromptData(), TestPromptBuilder_BuildDebaterR1(), TestPromptBuilder_BuildDebaterR1_NoSchema(), TestPromptBuilder_BuildDebaterR2(), TestPromptBuilder_BuildJudge(), TestPromptBuilder_BuildReviewer(), TestPromptBuilder_BuildReviewer_NoCodeContext(), TestPromptBuilder_ContextInjected() (+1 more)

### Community 187 - "Community 187"
Cohesion: 0.18
Nodes (0): 

### Community 188 - "Community 188"
Cohesion: 0.4
Nodes (4): OutputParser, extractJSON(), stripMarkdownJSON(), tryUnwrapClaudeEnvelope()

### Community 189 - "Community 189"
Cohesion: 0.18
Nodes (0): 

### Community 190 - "Community 190"
Cohesion: 0.18
Nodes (0): 

### Community 191 - "Community 191"
Cohesion: 0.49
Nodes (10): makeProject(), TestExtract_ExportedFunc(), TestExtract_GenericFunc(), TestExtract_GenericType(), TestExtract_InterfaceType(), TestExtract_Method(), TestExtract_StructType(), TestExtract_TestFilesSkipped() (+2 more)

### Community 192 - "Community 192"
Cohesion: 0.18
Nodes (0): 

### Community 193 - "Community 193"
Cohesion: 0.33
Nodes (7): docsCacheAdapter, detectLibrariesFromDir(), docsAutoDetect(), docsCacheDir(), docsOutput(), newDocsCmd(), newDocsFetchCmd()

### Community 194 - "Community 194"
Cohesion: 0.2
Nodes (0): 

### Community 195 - "Community 195"
Cohesion: 0.38
Nodes (9): newTerminalCmd(), newTerminalDetectCmd(), newTerminalNotifyCmd(), newTerminalSendCmd(), newTerminalSplitCmd(), newTerminalWorkspaceCmd(), newWorkspaceCloseCmd(), newWorkspaceCreateCmd() (+1 more)

### Community 196 - "Community 196"
Cohesion: 0.2
Nodes (0): 

### Community 197 - "Community 197"
Cohesion: 0.27
Nodes (4): buildTarGz(), TestDownloadAndVerify_ChecksumMismatch(), TestDownloadAndVerify_RetrySuccess(), TestDownloadAndVerify_Success()

### Community 198 - "Community 198"
Cohesion: 0.2
Nodes (0): 

### Community 199 - "Community 199"
Cohesion: 0.33
Nodes (9): GitHookScript, appendUniqueHook(), buildCommitMsgScript(), buildPreCommitScript(), DetectPermissions(), fileExists(), generateCLIHooks(), generateGitHooks() (+1 more)

### Community 200 - "Community 200"
Cohesion: 0.2
Nodes (0): 

### Community 201 - "Community 201"
Cohesion: 0.31
Nodes (6): ActivateSkills(), FormatActivationNotice(), isRegexTrigger(), matchSkill(), ActivationResult, SkillActivator

### Community 202 - "Community 202"
Cohesion: 0.2
Nodes (0): 

### Community 203 - "Community 203"
Cohesion: 0.29
Nodes (7): MethodologyDef, Stage, generateDDDInstruction(), generateDoubleDiamondInstruction(), generateGenericInstruction(), GenerateInstruction(), generateTDDInstruction()

### Community 204 - "Community 204"
Cohesion: 0.2
Nodes (0): 

### Community 205 - "Community 205"
Cohesion: 0.2
Nodes (0): 

### Community 206 - "Community 206"
Cohesion: 0.33
Nodes (6): subprocessBackend, buildSubprocessArgs(), setupStdin(), startWithFileInput(), startWithStdinPipe(), validateJSONOutput()

### Community 207 - "Community 207"
Cohesion: 0.2
Nodes (0): 

### Community 208 - "Community 208"
Cohesion: 0.24
Nodes (3): mockBackend, defaultOutput(), TestRunSubprocessPipeline_FastMode()

### Community 209 - "Community 209"
Cohesion: 0.2
Nodes (0): 

### Community 210 - "Community 210"
Cohesion: 0.2
Nodes (0): 

### Community 211 - "Community 211"
Cohesion: 0.2
Nodes (0): 

### Community 212 - "Community 212"
Cohesion: 0.2
Nodes (0): 

### Community 213 - "Community 213"
Cohesion: 0.2
Nodes (0): 

### Community 214 - "Community 214"
Cohesion: 0.2
Nodes (0): 

### Community 215 - "Community 215"
Cohesion: 0.31
Nodes (6): TestCheckAuthValidity_APIKey(), TestCheckAuthValidity_ExpiredJWT(), TestCheckAuthValidity_NoExpiryJWT(), TestCheckAuthValidity_UnparseableExpiry(), TestCheckAuthValidity_ValidJWT(), writeCredentials()

### Community 216 - "Community 216"
Cohesion: 0.2
Nodes (0): 

### Community 217 - "Community 217"
Cohesion: 0.24
Nodes (2): PhaseAllocation, PhaseAllocator

### Community 218 - "Community 218"
Cohesion: 0.36
Nodes (9): EnvResolveOptions, applySafeDefaults(), detectEnvFromProject(), goEnvVars(), isSecret(), isTTY(), loadTestEnvFile(), promptForSecret() (+1 more)

### Community 219 - "Community 219"
Cohesion: 0.2
Nodes (0): 

### Community 220 - "Community 220"
Cohesion: 0.2
Nodes (0): 

### Community 221 - "Community 221"
Cohesion: 0.22
Nodes (0): 

### Community 222 - "Community 222"
Cohesion: 0.36
Nodes (6): newTestLSPAdapter(), TestLSPClientAdapter_Definition(), TestLSPClientAdapter_Diagnostics(), TestLSPClientAdapter_References(), TestLSPClientAdapter_Rename(), TestLSPClientAdapter_Symbols()

### Community 223 - "Community 223"
Cohesion: 0.25
Nodes (2): makeDummyBinary(), TestResolvePlatform()

### Community 224 - "Community 224"
Cohesion: 0.22
Nodes (0): 

### Community 225 - "Community 225"
Cohesion: 0.36
Nodes (7): Framework, DetectFramework(), detectFrameworkFromPackageJSON(), detectGoFramework(), detectPythonFramework(), detectRustFramework(), mergeDeps()

### Community 226 - "Community 226"
Cohesion: 0.22
Nodes (0): 

### Community 227 - "Community 227"
Cohesion: 0.31
Nodes (4): sampleSettings(), TestClaudeJSON_RoundTrip(), TestCodexConfig_RoundTrip(), TestGeminiJSON_RoundTrip()

### Community 228 - "Community 228"
Cohesion: 0.39
Nodes (8): containsString(), EnsureOrchestraProvider(), MigrateOpencodeToCodex(), MigrateOrchestraConfig(), MigratePlatformNames(), PlatformToProvider(), ProviderToPlatform(), replaceInSlice()

### Community 229 - "Community 229"
Cohesion: 0.33
Nodes (6): countActiveFindings(), countEscapeHatch(), parseDiscoverFindings(), ParseVerdict(), parseVerifyFindings(), ShouldTripCircuitBreaker()

### Community 230 - "Community 230"
Cohesion: 0.39
Nodes (8): FileSizeExclusion, commonExclusions(), FileSizeExclusions(), frameworkExclusions(), goExclusions(), pythonExclusions(), rustExclusions(), typescriptExclusions()

### Community 231 - "Community 231"
Cohesion: 0.22
Nodes (0): 

### Community 232 - "Community 232"
Cohesion: 0.22
Nodes (1): execCommand

### Community 233 - "Community 233"
Cohesion: 0.22
Nodes (0): 

### Community 234 - "Community 234"
Cohesion: 0.22
Nodes (0): 

### Community 235 - "Community 235"
Cohesion: 0.22
Nodes (0): 

### Community 236 - "Community 236"
Cohesion: 0.22
Nodes (0): 

### Community 237 - "Community 237"
Cohesion: 0.28
Nodes (4): NewExtractorRegistry(), Extractor, ExtractorRegistry, tsExtractorDir

### Community 238 - "Community 238"
Cohesion: 0.22
Nodes (0): 

### Community 239 - "Community 239"
Cohesion: 0.22
Nodes (0): 

### Community 240 - "Community 240"
Cohesion: 0.36
Nodes (2): checkSymlink(), PolicyCache

### Community 241 - "Community 241"
Cohesion: 0.22
Nodes (0): 

### Community 242 - "Community 242"
Cohesion: 0.22
Nodes (0): 

### Community 243 - "Community 243"
Cohesion: 0.22
Nodes (0): 

### Community 244 - "Community 244"
Cohesion: 0.25
Nodes (2): CardBuilder, RegistrationResult

### Community 245 - "Community 245"
Cohesion: 0.28
Nodes (6): defaultCredentialDir(), migratePlaintextCredentials(), NewCredentialStore(), CredentialStore, Option, storeOptions

### Community 246 - "Community 246"
Cohesion: 0.33
Nodes (5): TestLoadAPIKey_WithAPIKey(), TestLoadAPIKey_WrongAuthType(), TestLoadAuthToken_APIKey(), TestLoadAuthToken_JWT(), writeTestCredentials()

### Community 247 - "Community 247"
Cohesion: 0.39
Nodes (2): RotatingWriter, NewRotatingWriter()

### Community 248 - "Community 248"
Cohesion: 0.22
Nodes (0): 

### Community 249 - "Community 249"
Cohesion: 0.5
Nodes (8): findProjectRoot(), makeGoModule(), TestExtractCobra_NestedSubcommands_ExtractsLeafOnly(), TestExtractCobra_NoEntryPoint_ReturnsEmpty(), TestExtractCobra_RealProject_ExtractsKnownCommands(), TestExtractCobra_SimpleCommand_ReturnsScenario(), TestExtractCobra_WithFlags_IncludesFlags(), writeGoFile()

### Community 250 - "Community 250"
Cohesion: 0.22
Nodes (0): 

### Community 251 - "Community 251"
Cohesion: 0.22
Nodes (0): 

### Community 252 - "Community 252"
Cohesion: 0.25
Nodes (0): 

### Community 253 - "Community 253"
Cohesion: 0.54
Nodes (6): chdir(), setupLearnDir(), TestLearnCmd_NoSubcommand_PrintsHelp(), TestLearnQuery_FlagParsing_MultipleFlags(), TestLearnQuery_NoEntries_PrintsNoMatching(), TestLearnQuery_UnknownFlag_ReturnsError()

### Community 254 - "Community 254"
Cohesion: 0.25
Nodes (0): 

### Community 255 - "Community 255"
Cohesion: 0.25
Nodes (0): 

### Community 256 - "Community 256"
Cohesion: 0.32
Nodes (3): formatTextLine(), NewPipelineLogger(), PipelineLogger

### Community 257 - "Community 257"
Cohesion: 0.25
Nodes (5): Event, EventType, Event, InitData, ResultData

### Community 258 - "Community 258"
Cohesion: 0.46
Nodes (1): Store

### Community 259 - "Community 259"
Cohesion: 0.25
Nodes (0): 

### Community 260 - "Community 260"
Cohesion: 0.25
Nodes (0): 

### Community 261 - "Community 261"
Cohesion: 0.39
Nodes (5): extractBinaryTarGz(), extractBinaryZip(), httpGetWithRetry(), ParseChecksums(), Downloader

### Community 262 - "Community 262"
Cohesion: 0.25
Nodes (0): 

### Community 263 - "Community 263"
Cohesion: 0.25
Nodes (0): 

### Community 264 - "Community 264"
Cohesion: 0.46
Nodes (7): cleanArg(), replaceAgentCalls(), replaceMCPCalls(), replacePaths(), ReplacePlatformReferences(), replaceTodoWrite(), replaceWorktreeIsolation()

### Community 265 - "Community 265"
Cohesion: 0.25
Nodes (0): 

### Community 266 - "Community 266"
Cohesion: 0.25
Nodes (1): StrategyFunc

### Community 267 - "Community 267"
Cohesion: 0.25
Nodes (0): 

### Community 268 - "Community 268"
Cohesion: 0.29
Nodes (2): consensusReached(), countNonEmpty()

### Community 269 - "Community 269"
Cohesion: 0.46
Nodes (6): findDifferences(), FormatDebate(), max1(), MergeConsensus(), normalizeLine(), splitLines()

### Community 270 - "Community 270"
Cohesion: 0.25
Nodes (0): 

### Community 271 - "Community 271"
Cohesion: 0.25
Nodes (0): 

### Community 272 - "Community 272"
Cohesion: 0.29
Nodes (5): NewExaClient(), NewExaClientFromEnv(), ExaClient, ExaOption, SearchResult

### Community 273 - "Community 273"
Cohesion: 0.25
Nodes (0): 

### Community 274 - "Community 274"
Cohesion: 0.25
Nodes (0): 

### Community 275 - "Community 275"
Cohesion: 0.46
Nodes (7): setupTestRepo(), TestCheckCleanWorktree(), TestCommitExperiment(), TestCreateExperimentBranch(), TestGetDiffStats(), TestIsExperimentBranch(), TestResetToCommit()

### Community 276 - "Community 276"
Cohesion: 0.25
Nodes (0): 

### Community 277 - "Community 277"
Cohesion: 0.39
Nodes (1): WorktreeManager

### Community 278 - "Community 278"
Cohesion: 0.25
Nodes (0): 

### Community 279 - "Community 279"
Cohesion: 0.25
Nodes (0): 

### Community 280 - "Community 280"
Cohesion: 0.25
Nodes (0): 

### Community 281 - "Community 281"
Cohesion: 0.25
Nodes (0): 

### Community 282 - "Community 282"
Cohesion: 0.5
Nodes (7): checkClaude(), checkCodex(), checkGemini(), checkOpencode(), CheckProviderAuth(), dirExists(), fileExists()

### Community 283 - "Community 283"
Cohesion: 0.32
Nodes (5): checkNPM(), DetectProviders(), detectVersion(), InstallProvider(), ProviderStatus

### Community 284 - "Community 284"
Cohesion: 0.25
Nodes (3): MCPConfig, MCPConfigOptions, MCPServerConfig

### Community 285 - "Community 285"
Cohesion: 0.25
Nodes (0): 

### Community 286 - "Community 286"
Cohesion: 0.25
Nodes (0): 

### Community 287 - "Community 287"
Cohesion: 0.29
Nodes (0): 

### Community 288 - "Community 288"
Cohesion: 0.29
Nodes (0): 

### Community 289 - "Community 289"
Cohesion: 0.29
Nodes (4): gateChecker, GateConfig, GateMode, GateResult

### Community 290 - "Community 290"
Cohesion: 0.29
Nodes (6): playwrightAttachment, playwrightResult, playwrightSpec, playwrightSuite, playwrightTest, playwrightTestResult

### Community 291 - "Community 291"
Cohesion: 0.29
Nodes (4): claudeOutput, codexOutput, geminiOutput, Phase

### Community 292 - "Community 292"
Cohesion: 0.38
Nodes (2): PhaseContext, PhasePromptBuilder

### Community 293 - "Community 293"
Cohesion: 0.52
Nodes (6): RecordCoverageGap(), recordEntry(), RecordExecutorError(), RecordFixPattern(), RecordGateFail(), RecordReviewIssue()

### Community 294 - "Community 294"
Cohesion: 0.29
Nodes (2): HintsConf, UsageProfile

### Community 295 - "Community 295"
Cohesion: 0.29
Nodes (0): 

### Community 296 - "Community 296"
Cohesion: 0.38
Nodes (3): DeduplicateFindings(), MergeSupermajority(), NormalizeScopeRef()

### Community 297 - "Community 297"
Cohesion: 0.38
Nodes (5): GolangciIssue, GolangciOutput, isNotFoundError(), ParseGolangciOutput(), RunStaticAnalysis()

### Community 298 - "Community 298"
Cohesion: 0.57
Nodes (6): buildSkillTemplate(), generateAgentTemplates(), GenerateAllTemplates(), generateSkillTemplates(), validateName(), writeSkillTemplate()

### Community 299 - "Community 299"
Cohesion: 0.29
Nodes (0): 

### Community 300 - "Community 300"
Cohesion: 0.48
Nodes (6): collectSearchDirs(), DetectContext(), detectLanguage(), detectMarkers(), extractExtensions(), ActivationContext

### Community 301 - "Community 301"
Cohesion: 0.52
Nodes (6): collapseBlankLines(), SanitizeScreenOutput(), stripANSIExtended(), stripCLIBanners(), stripStatusBar(), trimTrailingWhitespace()

### Community 302 - "Community 302"
Cohesion: 0.29
Nodes (0): 

### Community 303 - "Community 303"
Cohesion: 0.48
Nodes (3): SchemaBuilder, buildSchema(), fieldSchema()

### Community 304 - "Community 304"
Cohesion: 0.29
Nodes (3): YieldOutput, YieldResponse, YieldRound

### Community 305 - "Community 305"
Cohesion: 0.52
Nodes (6): codexAgentPipelineSkillBody(), codexAgentTeamsSkillBody(), codexSubagentDevSkillBody(), codexWorktreeIsolationSkillBody(), normalizeCodexExtendedSkill(), rewriteCodexPRDSkillBody()

### Community 306 - "Community 306"
Cohesion: 0.33
Nodes (2): countingFetcher, TestFetcher_AllSourcesFail()

### Community 307 - "Community 307"
Cohesion: 0.29
Nodes (1): CircuitBreaker

### Community 308 - "Community 308"
Cohesion: 0.57
Nodes (5): gitOutputForTest(), initGitRepoWithOrigin(), runGit(), TestVerifyExecutionPostconditions_PushBranchExistsPasses(), TestVerifyExecutionPostconditions_PushBranchMissingFails()

### Community 309 - "Community 309"
Cohesion: 0.52
Nodes (6): extractFiles(), extractSections(), Summarize(), truncateToTokens(), writeFileSection(), writeSection()

### Community 310 - "Community 310"
Cohesion: 0.29
Nodes (0): 

### Community 311 - "Community 311"
Cohesion: 0.29
Nodes (3): ContextCompressor, DefaultCompressor, NopCompressor

### Community 312 - "Community 312"
Cohesion: 0.29
Nodes (1): TaskSemaphore

### Community 313 - "Community 313"
Cohesion: 0.29
Nodes (0): 

### Community 314 - "Community 314"
Cohesion: 0.43
Nodes (6): renderApprovalDialog(), renderApprovalKeys(), renderRiskBadge(), wrapText(), ApprovalRequest, ApprovalResult

### Community 315 - "Community 315"
Cohesion: 0.48
Nodes (5): renderChildren(), renderNode(), RenderTree(), statusIcon(), SubagentNode

### Community 316 - "Community 316"
Cohesion: 0.29
Nodes (0): 

### Community 317 - "Community 317"
Cohesion: 0.29
Nodes (0): 

### Community 318 - "Community 318"
Cohesion: 0.57
Nodes (6): ensureDeviceAuth(), ensureInstallDaemon(), EnsureWorker(), saveTokenCredentials(), tryRefreshCredentials(), EnsureResult

### Community 319 - "Community 319"
Cohesion: 0.48
Nodes (5): contains(), ParseCron(), parseField(), parsePart(), CronExpr

### Community 320 - "Community 320"
Cohesion: 0.29
Nodes (0): 

### Community 321 - "Community 321"
Cohesion: 0.48
Nodes (5): freePort(), TestStartOAuthFlow_PortIsValid(), TestWaitForCallback_ContextCancelled(), TestWaitForCallback_ErrorPath(), TestWaitForCallback_SuccessPath()

### Community 322 - "Community 322"
Cohesion: 0.29
Nodes (0): 

### Community 323 - "Community 323"
Cohesion: 0.33
Nodes (0): 

### Community 324 - "Community 324"
Cohesion: 0.33
Nodes (0): 

### Community 325 - "Community 325"
Cohesion: 0.33
Nodes (0): 

### Community 326 - "Community 326"
Cohesion: 0.33
Nodes (0): 

### Community 327 - "Community 327"
Cohesion: 0.53
Nodes (5): packageJSON, detectFromPackageJSON(), DetectTestRunner(), fileExists(), hasPytest()

### Community 328 - "Community 328"
Cohesion: 0.47
Nodes (5): TeamDashboardData, TeammateStatus, NewTeammateStatus(), RenderTeamDashboard(), teammateIcon()

### Community 329 - "Community 329"
Cohesion: 0.33
Nodes (0): 

### Community 330 - "Community 330"
Cohesion: 0.33
Nodes (0): 

### Community 331 - "Community 331"
Cohesion: 0.33
Nodes (0): 

### Community 332 - "Community 332"
Cohesion: 0.33
Nodes (0): 

### Community 333 - "Community 333"
Cohesion: 0.33
Nodes (0): 

### Community 334 - "Community 334"
Cohesion: 0.33
Nodes (0): 

### Community 335 - "Community 335"
Cohesion: 0.47
Nodes (4): isBuildFileName(), Validate(), ValidateCommands(), validateDocFile()

### Community 336 - "Community 336"
Cohesion: 0.33
Nodes (0): 

### Community 337 - "Community 337"
Cohesion: 0.33
Nodes (0): 

### Community 338 - "Community 338"
Cohesion: 0.53
Nodes (4): assignAutoIDs(), normalizeKeyword(), ParseGherkin(), scenarioBuilder

### Community 339 - "Community 339"
Cohesion: 0.4
Nodes (3): IntentRule, GenerateIntentGateInstruction(), sortRulesByPriority()

### Community 340 - "Community 340"
Cohesion: 0.6
Nodes (5): badArgsProvider(), emptyOutputProvider(), TestRunDebate_JudgeRunsWithPartialResponses(), TestRunParallel_EmptyOutputProviders_AreReportedAsFailed(), TestRunProvider_EmptyOutput_IsAnError()

### Community 341 - "Community 341"
Cohesion: 0.33
Nodes (0): 

### Community 342 - "Community 342"
Cohesion: 0.4
Nodes (3): MergeSubprocessResults(), truncate(), JudgeBuilder

### Community 343 - "Community 343"
Cohesion: 0.33
Nodes (0): 

### Community 344 - "Community 344"
Cohesion: 0.33
Nodes (0): 

### Community 345 - "Community 345"
Cohesion: 0.33
Nodes (0): 

### Community 346 - "Community 346"
Cohesion: 0.33
Nodes (0): 

### Community 347 - "Community 347"
Cohesion: 0.47
Nodes (2): Fetcher, cacheKey()

### Community 348 - "Community 348"
Cohesion: 0.4
Nodes (1): TSExtractor

### Community 349 - "Community 349"
Cohesion: 0.4
Nodes (4): stripSingleQuoted(), ValidateCommand(), validateConfig, ValidateOption

### Community 350 - "Community 350"
Cohesion: 0.53
Nodes (4): agentSummary(), FormatComparison(), formatDuration(), FormatSummary()

### Community 351 - "Community 351"
Cohesion: 0.67
Nodes (5): FilterByType(), LatestPipelineRun(), LoadAllEvents(), LoadEvents(), PipelineRunsBySpecID()

### Community 352 - "Community 352"
Cohesion: 0.4
Nodes (2): buildKnowledgeQuery(), populateKnowledge()

### Community 353 - "Community 353"
Cohesion: 0.6
Nodes (5): CountToolBlocks(), PruneAndReport(), pruneBlocks(), PruneSummary(), PruneToolResults()

### Community 354 - "Community 354"
Cohesion: 0.33
Nodes (0): 

### Community 355 - "Community 355"
Cohesion: 0.33
Nodes (0): 

### Community 356 - "Community 356"
Cohesion: 0.33
Nodes (1): keychainStore

### Community 357 - "Community 357"
Cohesion: 0.47
Nodes (1): TaskPoller

### Community 358 - "Community 358"
Cohesion: 0.33
Nodes (0): 

### Community 359 - "Community 359"
Cohesion: 0.47
Nodes (3): WarningInjector, formatDanger(), formatWarning()

### Community 360 - "Community 360"
Cohesion: 0.33
Nodes (0): 

### Community 361 - "Community 361"
Cohesion: 0.4
Nodes (4): Scenario, ScenarioSet, renderBuildLine(), RenderScenarios()

### Community 362 - "Community 362"
Cohesion: 0.8
Nodes (4): loadSkillRegistry(), newSkillCmd(), runSkillInfo(), runSkillList()

### Community 363 - "Community 363"
Cohesion: 0.4
Nodes (0): 

### Community 364 - "Community 364"
Cohesion: 0.6
Nodes (4): scenarioJSONResult, newAutoTestCmd(), newAutoTestRunCmd(), runAutoTest()

### Community 365 - "Community 365"
Cohesion: 0.4
Nodes (0): 

### Community 366 - "Community 366"
Cohesion: 0.6
Nodes (3): TestTestRunCmd_JSONOutput_FormatsCorrectly(), TestTestRunCmd_ValidProject_Succeeds(), writeScenariosFile()

### Community 367 - "Community 367"
Cohesion: 0.6
Nodes (3): TestSkillInfoCmd(), TestSkillListCmd(), writeTestSkill()

### Community 368 - "Community 368"
Cohesion: 0.4
Nodes (0): 

### Community 369 - "Community 369"
Cohesion: 0.4
Nodes (0): 

### Community 370 - "Community 370"
Cohesion: 0.4
Nodes (0): 

### Community 371 - "Community 371"
Cohesion: 0.4
Nodes (0): 

### Community 372 - "Community 372"
Cohesion: 0.4
Nodes (0): 

### Community 373 - "Community 373"
Cohesion: 0.5
Nodes (3): ModelPricing, ModelForAgent(), QualityModeToModels()

### Community 374 - "Community 374"
Cohesion: 0.4
Nodes (0): 

### Community 375 - "Community 375"
Cohesion: 0.4
Nodes (0): 

### Community 376 - "Community 376"
Cohesion: 0.4
Nodes (0): 

### Community 377 - "Community 377"
Cohesion: 0.4
Nodes (4): JudgeResult, PreviousResult, PromptData, RelevantPath

### Community 378 - "Community 378"
Cohesion: 0.4
Nodes (0): 

### Community 379 - "Community 379"
Cohesion: 0.5
Nodes (2): shellEscapeArg(), shellEscapeArgs()

### Community 380 - "Community 380"
Cohesion: 0.4
Nodes (0): 

### Community 381 - "Community 381"
Cohesion: 0.7
Nodes (4): Sanitize(), SanitizeGitURL(), SanitizePath(), SanitizeSecrets()

### Community 382 - "Community 382"
Cohesion: 0.4
Nodes (0): 

### Community 383 - "Community 383"
Cohesion: 0.4
Nodes (0): 

### Community 384 - "Community 384"
Cohesion: 0.4
Nodes (0): 

### Community 385 - "Community 385"
Cohesion: 0.4
Nodes (2): Excluder, pattern

### Community 386 - "Community 386"
Cohesion: 0.4
Nodes (1): noopDetector

### Community 387 - "Community 387"
Cohesion: 0.6
Nodes (1): Reaper

### Community 388 - "Community 388"
Cohesion: 0.4
Nodes (1): unixDetector

### Community 389 - "Community 389"
Cohesion: 0.4
Nodes (2): ClassificationSignals, MessageComplexityClassifier

### Community 390 - "Community 390"
Cohesion: 0.4
Nodes (1): BuildEntry

### Community 391 - "Community 391"
Cohesion: 0.4
Nodes (0): 

### Community 392 - "Community 392"
Cohesion: 0.83
Nodes (3): buildBrainstormPrompt(), newOrchestraBrainstormCmd(), prependProjectContext()

### Community 393 - "Community 393"
Cohesion: 0.83
Nodes (3): newWorkerCmd(), newWorkerValidateSubCmd(), runWorkerValidate()

### Community 394 - "Community 394"
Cohesion: 0.67
Nodes (2): requireNoError(), TestResolveProvider_PrefersAuthenticatedConfiguredProvider()

### Community 395 - "Community 395"
Cohesion: 0.5
Nodes (1): SummaryRow

### Community 396 - "Community 396"
Cohesion: 0.83
Nodes (3): hasFailedTask(), MapCheckpointToPhases(), resolvePhaseStatus()

### Community 397 - "Community 397"
Cohesion: 0.67
Nodes (2): expandEnvVars(), Load()

### Community 398 - "Community 398"
Cohesion: 0.5
Nodes (0): 

### Community 399 - "Community 399"
Cohesion: 0.67
Nodes (2): ParseTrailers(), setField()

### Community 400 - "Community 400"
Cohesion: 0.5
Nodes (0): 

### Community 401 - "Community 401"
Cohesion: 0.5
Nodes (0): 

### Community 402 - "Community 402"
Cohesion: 0.5
Nodes (0): 

### Community 403 - "Community 403"
Cohesion: 0.5
Nodes (0): 

### Community 404 - "Community 404"
Cohesion: 0.67
Nodes (2): MergeStructuredConsensus(), parseStructuredResponse()

### Community 405 - "Community 405"
Cohesion: 0.5
Nodes (0): 

### Community 406 - "Community 406"
Cohesion: 0.5
Nodes (0): 

### Community 407 - "Community 407"
Cohesion: 0.5
Nodes (0): 

### Community 408 - "Community 408"
Cohesion: 0.67
Nodes (2): indexOfSubstring(), TestFormat_MultipleLibraries()

### Community 409 - "Community 409"
Cohesion: 0.5
Nodes (0): 

### Community 410 - "Community 410"
Cohesion: 0.5
Nodes (0): 

### Community 411 - "Community 411"
Cohesion: 0.5
Nodes (0): 

### Community 412 - "Community 412"
Cohesion: 0.5
Nodes (1): GoExtractor

### Community 413 - "Community 413"
Cohesion: 0.5
Nodes (0): 

### Community 414 - "Community 414"
Cohesion: 0.5
Nodes (0): 

### Community 415 - "Community 415"
Cohesion: 0.5
Nodes (0): 

### Community 416 - "Community 416"
Cohesion: 0.67
Nodes (2): cacheSecurityPolicy(), policyDir()

### Community 417 - "Community 417"
Cohesion: 0.5
Nodes (0): 

### Community 418 - "Community 418"
Cohesion: 0.67
Nodes (3): HumanError(), HumanErrorf(), errorMapping

### Community 419 - "Community 419"
Cohesion: 0.5
Nodes (0): 

### Community 420 - "Community 420"
Cohesion: 0.5
Nodes (0): 

### Community 421 - "Community 421"
Cohesion: 0.5
Nodes (1): HeadlessEvent

### Community 422 - "Community 422"
Cohesion: 0.5
Nodes (0): 

### Community 423 - "Community 423"
Cohesion: 1.0
Nodes (2): newCheckCmd(), runChecks()

### Community 424 - "Community 424"
Cohesion: 0.67
Nodes (0): 

### Community 425 - "Community 425"
Cohesion: 1.0
Nodes (2): a2aSignPolicyForTest(), TestRunWorkerValidate_VerifiesPolicySignature()

### Community 426 - "Community 426"
Cohesion: 0.67
Nodes (0): 

### Community 427 - "Community 427"
Cohesion: 0.67
Nodes (0): 

### Community 428 - "Community 428"
Cohesion: 0.67
Nodes (0): 

### Community 429 - "Community 429"
Cohesion: 0.67
Nodes (0): 

### Community 430 - "Community 430"
Cohesion: 1.0
Nodes (2): DetectSystemLang(), matchLang()

### Community 431 - "Community 431"
Cohesion: 0.67
Nodes (0): 

### Community 432 - "Community 432"
Cohesion: 1.0
Nodes (2): Load(), LoadWithHash()

### Community 433 - "Community 433"
Cohesion: 0.67
Nodes (1): GateType

### Community 434 - "Community 434"
Cohesion: 1.0
Nodes (2): formatReviewMd(), PersistReview()

### Community 435 - "Community 435"
Cohesion: 0.67
Nodes (0): 

### Community 436 - "Community 436"
Cohesion: 1.0
Nodes (2): containsPlatformRef(), FilterPlatformReferences()

### Community 437 - "Community 437"
Cohesion: 0.67
Nodes (1): HookInput

### Community 438 - "Community 438"
Cohesion: 0.67
Nodes (0): 

### Community 439 - "Community 439"
Cohesion: 1.0
Nodes (2): extractLayer(), Lint()

### Community 440 - "Community 440"
Cohesion: 0.67
Nodes (0): 

### Community 441 - "Community 441"
Cohesion: 0.67
Nodes (0): 

### Community 442 - "Community 442"
Cohesion: 0.67
Nodes (1): workerKeyResponse

### Community 443 - "Community 443"
Cohesion: 0.67
Nodes (1): AuditMetadata

### Community 444 - "Community 444"
Cohesion: 1.0
Nodes (0): 

### Community 445 - "Community 445"
Cohesion: 1.0
Nodes (0): 

### Community 446 - "Community 446"
Cohesion: 1.0
Nodes (0): 

### Community 447 - "Community 447"
Cohesion: 1.0
Nodes (0): 

### Community 448 - "Community 448"
Cohesion: 1.0
Nodes (0): 

### Community 449 - "Community 449"
Cohesion: 1.0
Nodes (0): 

### Community 450 - "Community 450"
Cohesion: 1.0
Nodes (0): 

### Community 451 - "Community 451"
Cohesion: 1.0
Nodes (0): 

### Community 452 - "Community 452"
Cohesion: 1.0
Nodes (0): 

### Community 453 - "Community 453"
Cohesion: 1.0
Nodes (0): 

### Community 454 - "Community 454"
Cohesion: 1.0
Nodes (0): 

### Community 455 - "Community 455"
Cohesion: 1.0
Nodes (0): 

### Community 456 - "Community 456"
Cohesion: 1.0
Nodes (0): 

### Community 457 - "Community 457"
Cohesion: 1.0
Nodes (0): 

### Community 458 - "Community 458"
Cohesion: 1.0
Nodes (0): 

### Community 459 - "Community 459"
Cohesion: 1.0
Nodes (0): 

### Community 460 - "Community 460"
Cohesion: 1.0
Nodes (0): 

### Community 461 - "Community 461"
Cohesion: 1.0
Nodes (0): 

### Community 462 - "Community 462"
Cohesion: 1.0
Nodes (0): 

### Community 463 - "Community 463"
Cohesion: 1.0
Nodes (0): 

### Community 464 - "Community 464"
Cohesion: 1.0
Nodes (0): 

### Community 465 - "Community 465"
Cohesion: 1.0
Nodes (0): 

### Community 466 - "Community 466"
Cohesion: 1.0
Nodes (0): 

### Community 467 - "Community 467"
Cohesion: 1.0
Nodes (0): 

### Community 468 - "Community 468"
Cohesion: 1.0
Nodes (0): 

### Community 469 - "Community 469"
Cohesion: 1.0
Nodes (0): 

### Community 470 - "Community 470"
Cohesion: 1.0
Nodes (0): 

### Community 471 - "Community 471"
Cohesion: 1.0
Nodes (0): 

### Community 472 - "Community 472"
Cohesion: 1.0
Nodes (0): 

### Community 473 - "Community 473"
Cohesion: 1.0
Nodes (0): 

### Community 474 - "Community 474"
Cohesion: 1.0
Nodes (0): 

### Community 475 - "Community 475"
Cohesion: 1.0
Nodes (0): 

### Community 476 - "Community 476"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **444 isolated node(s):** `taskContext`, `taskResult`, `execFunc`, `globalFlags`, `globalFlagsContextKey` (+439 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 444`** (2 nodes): `main.go`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (2 nodes): `init_constraints.go`, `generateDefaultConstraints()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 446`** (2 nodes): `wizard_styles.go`, `AutopusTheme()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 447`** (2 nodes): `wizard_profile.go`, `buildProfileStep()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (2 nodes): `branchvalidate.go`, `ValidateBranchName()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 449`** (2 nodes): `prune.go`, `Prune()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 450`** (2 nodes): `summary.go`, `GenerateSummary()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 451`** (2 nodes): `rewrite.go`, `rewriteStore()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 452`** (2 nodes): `defaults.go`, `DefaultFullConfig()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 453`** (2 nodes): `writer.go`, `BuildCommit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 454`** (2 nodes): `scenarios.go`, `generateScenarios()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 455`** (2 nodes): `ax.go`, `GenerateAXInstruction()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 456`** (2 nodes): `agent_transformer_condense.go`, `condenseBody()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 457`** (2 nodes): `screen_sanitizer_test.go`, `TestSanitizeScreenOutput()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 458`** (2 nodes): `writeutil.go`, `WriteFileIfChanged()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 459`** (2 nodes): `generator.go`, `Generate()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 460`** (2 nodes): `simplicity.go`, `CalculateSimplicity()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 461`** (2 nodes): `computer_use.go`, `ComputerUseSupported()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 462`** (2 nodes): `validate_normalize.go`, `NormalizeCommand()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 463`** (2 nodes): `emergency_unix.go`, `sendSignal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 464`** (2 nodes): `emergency_helper_test.go`, `sysProcAttr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 465`** (2 nodes): `emergency_windows.go`, `sendSignal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 466`** (2 nodes): `classifier_test.go`, `TestClassify()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 467`** (2 nodes): `pidlock_internal_test.go`, `TestAcquire_FlockError()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 468`** (2 nodes): `flock_unix.go`, `isProcessAlive()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 469`** (1 nodes): `embed.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 470`** (1 nodes): `export_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 471`** (1 nodes): `hook-opencode-complete.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 472`** (1 nodes): `detect_stdlib.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 473`** (1 nodes): `loop_audit_helpers_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 474`** (1 nodes): `server_approval.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (1 nodes): `server_helpers.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 476`** (1 nodes): `credstore_testmain_test.go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Adapter` connect `Community 15` to `Community 0`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **Why does `Adapter` connect `Community 24` to `Community 0`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `taskContext`, `taskResult`, `execFunc` to the rest of the system?**
  _444 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._