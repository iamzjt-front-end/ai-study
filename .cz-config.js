'use strict';

module.exports = {
  types: [
    { value: 'feat', name: '✨ feat:     新功能' },
    { value: 'fix', name: '🐛 fix:      修复Bug' },
    { value: 'docs', name: '📝 docs:     文档修改' },
    { value: 'style', name: '💄 style:    代码格式（不影响逻辑）' },
    { value: 'refactor', name: '♻️ refactor: 代码重构' },
    { value: 'perf', name: '⚡️ perf:     性能优化' },
    { value: 'test', name: '✅ test:     添加或修改测试' },
    { value: 'chore', name: '🔧 chore:    构建/依赖/脚本调整' },
    { value: 'revert', name: '⏪ revert:   回退提交' }
  ],

  messages: {
    type: '请选择提交类型（带表情）：',
    scope: '请输入影响范围（可选，比如模块名）：',
    subject: '请输入简短描述（建议一句话）：',
    body: '请输入详细说明（可选）：',
    footer: '请输入要关闭的 Issue（可选）：',
    confirmCommit: '确认提交吗？'
  },

  scopes: [
    { name: 'ui' },
    { name: 'api' },
    { name: 'utils' },
    { name: 'config' },
    { name: 'docs' }
  ],

  allowCustomScopes: true,
  allowBreakingChanges: false, // ❌ 禁用“BREAKING CHANGES”功能
  skipQuestions: ['body', 'footer', 'breaking'], // ✅ 跳过对应问题
  subjectLimit: 100
};
