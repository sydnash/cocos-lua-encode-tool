
local data = {
	remoteUrl = 'http://127.0.0.1:8000/resinfo.lua',
	version = '1.1.2',

	resUrl = 'http://127.0.0.1:8000/',
	resDict = {
		['src/main.lua'] =  {md5 = '...', compress = false},
		['src/app/MyApp.lua'] = {md5 = '...', compress = false},
		['src/app/views/scheduler.lua'] = {md5 = '...', compress = false},
		['src/packages/mvc/init.lua'] = {md5 = '...', compress = false},
	},
}

return data