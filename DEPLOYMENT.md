# 🚀 部署指南 - 洛谷题目浏览站

## 📋 部署到Netlify

### 1. **准备工作**

确保你的项目包含以下文件：
- `netlify.toml` - Netlify配置文件 ✅
- `package.json` - Node.js依赖配置 ✅
- `netlify/functions/trigger-workflow.js` - 工作流触发函数 ✅

### 2. **部署步骤**

#### 方式一：通过Netlify Web界面部署
1. 登录 [Netlify](https://netlify.com)
2. 点击 "New site from Git"
3. 选择你的GitHub仓库 `CB-X2-Jun/luogu-problem-reader`
4. 配置构建设置：
   - **Build command**: `echo 'No build step required'`
   - **Publish directory**: `.` (根目录)
   - **Functions directory**: `netlify/functions`

#### 方式二：通过Netlify CLI部署
```bash
# 安装Netlify CLI
npm install -g netlify-cli

# 登录Netlify
netlify login

# 初始化站点
netlify init

# 部署
netlify deploy --prod
```

### 3. **环境变量配置**

在Netlify控制台中设置以下环境变量：

- **`GITHUB_TOKEN`**: GitHub Personal Access Token
  - 权限需要：`repo`, `actions:write`
  - 获取地址：https://github.com/settings/tokens

### 4. **GitHub Token配置步骤**

1. 访问 GitHub Settings → Developer settings → Personal access tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：
   - ✅ `repo` (完整仓库访问)
   - ✅ `workflow` (更新GitHub Actions工作流)
4. 复制生成的token
5. 在Netlify站点设置中添加环境变量 `GITHUB_TOKEN`

### 5. **验证部署**

部署完成后，访问你的Netlify站点：
1. 检查首页是否正常加载
2. 点击自动化控制面板中的按钮
3. 验证工作流是否能成功触发

### 6. **故障排除**

#### 常见问题：

**问题1**: 工作流触发失败
- 检查 `GITHUB_TOKEN` 是否正确设置
- 确认token权限包含 `workflow` 和 `repo`
- 查看Netlify Functions日志

**问题2**: CORS错误
- 确认 `netlify.toml` 中的CORS配置正确
- 检查函数是否正确处理OPTIONS请求

**问题3**: 函数超时
- Netlify Functions默认超时时间为10秒
- 如需更长时间，升级到Pro计划

### 7. **自定义域名**（可选）

1. 在Netlify控制台中点击 "Domain settings"
2. 添加自定义域名
3. 配置DNS记录指向Netlify

## 🎯 功能特性

部署完成后，用户可以：

- 📊 **查看实时统计**: 题目总数、样例覆盖率等
- 🎨 **触发主题更新**: 根据季节和节日自动切换主题
- 🔍 **执行SEO优化**: 更新sitemap和meta标签
- 📈 **生成数据可视化**: 创建统计图表和仪表板
- 🔄 **实时反馈**: 查看工作流执行状态

## 📞 技术支持

如遇到问题，请：
1. 查看Netlify Functions日志
2. 检查GitHub Actions运行状态
3. 确认环境变量配置正确

---

🎉 **恭喜！你的洛谷题目浏览站现在具备了完整的自动化控制功能！**
